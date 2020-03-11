from django.conf import settings


def settings_export(request):
    api_prefix = settings.API_PREFIX

    return {
        'API_ROOT_URL': request.build_absolute_uri(api_prefix)
    }
