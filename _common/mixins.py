from rest_framework import exceptions, status, views, response
from _common.utils import get_response


class APIViewMixin(views.APIView):
    def handle_exception(self, exc):
        if isinstance(exc, (exceptions.NotAuthenticated, exceptions.AuthenticationFailed)):
            auth_header = self.get_authenticate_header(self.request)

            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN

        exception_handler = self.get_exception_handler()

        context = self.get_exception_handler_context()
        exc_response = exception_handler(exc, context)

        if exc_response is None:
            self.raise_uncaught_exception(exc)

            return response.Response({
                'success': False,
                'code': 'internal_server_error',
                'message': u'Internal Server Error',
                'result': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        exc_response.exception = True

        exc_response.data = {
            'success': False,
            'code': exc.default_code,
            'message': exc_response.reason_phrase,
            'result': exc_response.data
        }

        return exc_response

    def get_response(self, success=True, message='Success', result=None, detail_code='success', status_code=status.HTTP_200_OK):
        return get_response(success=success, message=message, result=result, detail_code=detail_code, status_code=status_code)


class PaginationMixin(views.APIView):
    pagination_default_page = 1
    pagination_default_limit = 16

    def paginate_queryset(self, queryset):
        page = self.request.data.get('page', self.pagination_default_page)
        limit = self.request.data.get('limit', self.pagination_default_limit)

        try:
            page = int(page)
            if page < 1:
                raise ValueError('Value Cannot be less than one')

        except ValueError:
            page = self.pagination_default_page

        try:
            limit = int(limit)
            if limit < 1:
                raise ValueError('Value Cannot be less than one')

        except ValueError:
            limit = self.pagination_default_limit

        records_per_page = limit
        offset = (page - 1) * records_per_page


        queryset = list(queryset[offset:records_per_page + 1])

        result_count = len(queryset)
        queryset = queryset[:records_per_page]
        last_page = result_count == len(queryset)
        result_count = len(queryset)

        serializer = self.get_serializer(queryset, many=True)

        json_data = serializer.data
        request_data = {
            'page': page,
            'count': result_count,
            'next': page + 1 if not last_page else None,
            'prev': page - 1 if page > 1 else None,
            'list': json_data,
        }
        return request_data
