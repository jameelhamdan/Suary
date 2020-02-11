from ..backend.settings import api_settings
from ..backend.jwt import verify_auth_token, verify_refresh_token
from ..backend.utils import AuthException, ForbiddenException, get_auth_header
from _common.errors import handler401, handler403

VERIFY_TYPES = api_settings.VERIFY_TYPES

VERIFY_TYPE_AUTH = api_settings.VERIFY_TYPE_AUTH
VERIFY_TYPE_ANY = api_settings.VERIFY_TYPE_ANY
VERIFY_TYPE_REFRESH = api_settings.VERIFY_TYPE_REFRESH


class AuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        try:
            auth_type = getattr(view_func, '_auth_type', None)
            if auth_type not in VERIFY_TYPES:
                raise AuthException()

            user = _http_auth_helper(request, auth_type)
            setattr(request, 'current_user', user)
            setattr(request, 'user', user)

            custom_method = getattr(view_func, '_custom_auth_method', None)
            if custom_method and not custom_method():
                raise ForbiddenException()

        except AuthException:
            return handler401(request, *view_args, **view_kwargs)

        except ForbiddenException:
            return handler403(request, *view_args, **view_kwargs)

        return view_func(request, *view_args, **view_kwargs)

    def __call__(self, request):
        response = self.get_response(request)
        return response


def _http_auth_helper(request, auth_type):
    try:
        if auth_type == VERIFY_TYPE_ANY:
            return None
        else:

            token = get_auth_header(request)
            if auth_type == VERIFY_TYPE_AUTH:
                return verify_auth_token(token)

            elif auth_type == VERIFY_TYPE_REFRESH:
                return verify_refresh_token(token)

        raise AuthException()

    except Exception as e:
        raise AuthException(e)
