from functools import wraps
from ..backend.settings import api_settings
from ..backend.utils import AuthErrorException
from django.utils.decorators import method_decorator


def _auth_user(auth_type=api_settings.VERIFY_TYPE_AUTH, custom_auth_method_name=None):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(*args, **kwargs):
            return view_func(*args, **kwargs)

        wrapped_view._auth_type = auth_type

        if custom_auth_method_name:
            custom_auth_method = getattr(wrapped_view, 'custom_auth_method_name', None)
            if not custom_auth_method:
                raise AuthErrorException('Method specified does not exist in view!')

            if not hasattr(custom_auth_method, '__call__'):
                raise AuthErrorException('Method specified is not a method?')

            # Save method in view as callable function
            # Should return boolean: True or False
            wrapped_view._custom_auth_method = custom_auth_method

        return wraps(view_func)(wrapped_view)

    return decorator


def view_allow_any():
    return method_decorator(_auth_user(auth_type=api_settings.VERIFY_TYPE_ANY), name='dispatch')


def view_authenticate():
    return method_decorator(_auth_user(auth_type=api_settings.VERIFY_TYPE_AUTH), name='dispatch')


def view_authenticate_refresh():
    return method_decorator(_auth_user(auth_type=api_settings.VERIFY_TYPE_REFRESH), name='dispatch')
