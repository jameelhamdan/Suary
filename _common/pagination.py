from collections import OrderedDict
from rest_framework import pagination
from _common.utils import get_response


class CustomPagination(pagination.CursorPagination, object):
    # Class override with object to allow passing of custom settings for each CustomPagination instance
    page_size = 16
    page_size_query_param = 'limit'
    max_page_size = 128
    ordering = '-created_on'
    message = 'Got Paginated List Successfully'
    overridable_attrs = ['message', 'ordering', 'page_size', 'page_size_query_param']

    def get_paginated_response(self, data):
        response_data = OrderedDict([
            ('page_size', self.page_size),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('list', data)
        ])

        return get_response(message=self.message, result=response_data)

    def __init__(self, **kwargs):
        for attr in self.overridable_attrs:
            attr_value = kwargs.get(attr)
            if attr_value is not None:
                setattr(self, attr, attr_value)

    def __call__(self):
        return self
