from django.conf import settings
from urllib.parse import   urljoin, urlsplit
from django.utils.encoding import  iri_to_uri


def build_base_url(request, location):
    if location is None:
        location = '//%s' % request.get_full_path()
    bits = urlsplit(location)
    if not (bits.scheme and bits.netloc):
        if (bits.path.startswith('/') and not bits.scheme and not bits.netloc and
                '/./' not in bits.path and '/../' not in bits.path):
            if location.startswith('//'):
                location = location[2:]
            location = request._current_scheme_host + location
        else:
            location = urljoin(request._current_scheme_host, location)
    return iri_to_uri(location)


def settings_export(request):
    api_prefix = settings.API_PREFIX

    return {
        'API_ROOT_URL': build_base_url(request, api_prefix)
    }
