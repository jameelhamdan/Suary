import uuid


def generate_uuid():
    return uuid.uuid4().hex


def stream_response(request, response, content_length):
    http_range = request.META.get('HTTP_RANGE')
    if not (http_range and http_range.startswith('bytes=') and http_range.count('-') == 1):
        return response
    if_range = request.META.get('HTTP_IF_RANGE')
    if if_range and if_range != response.get('Last-Modified') and if_range != response.get('ETag'):
        return response
    f = response.file_to_stream

    st_size = content_length

    start, end = http_range.split('=')[1].split('-')
    if not start:  # requesting the last N bytes
        start = max(0, st_size - int(end))
        end = ''
    start, end = int(start or 0), int(end or st_size - 1)
    assert 0 <= start < st_size, (start, st_size)
    end = min(end, st_size - 1)
    f.seek(start)
    old_read = f.read
    f.read = lambda n: old_read(min(n, end + 1 - f.tell()))
    response.status_code = 206
    response['Content-Length'] = end + 1 - start
    response['Content-Range'] = 'bytes %d-%d/%d' % (start, end, st_size)
    return response
