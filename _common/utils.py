from django.http import JsonResponse
from django.utils import timezone
from rest_framework import response, status
import uuid
import hashlib
import binascii
import os


def generate_uuid(repeat=1):
    final_uuid = ''
    for i in range(0, repeat):
        final_uuid += uuid.uuid4().hex

    return final_uuid


def stream_response(request, response, content_length, is_stream=True):
    http_range = request.META.get('HTTP_RANGE')
    if not (http_range and http_range.startswith('bytes=') and http_range.count('-') == 1):
        return response
    if_range = request.META.get('HTTP_IF_RANGE')
    if if_range and if_range != response.get('Last-Modified') and if_range != response.get('ETag'):
        return response
    f = response.file_to_stream

    st_size = content_length

    if is_stream:
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


def cache_response(r):
    r['cache-control'] = 'max-age=604800, s-maxage=604800, must-revalidate'
    r['expires'] = timezone.now() + timezone.timedelta(days=7)
    return r


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwd_hash = binascii.hexlify(pwd_hash)
    return (salt + pwd_hash).decode('ascii')


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwd_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'),  salt.encode('ascii'), 100000)
    pwd_hash = binascii.hexlify(pwd_hash).decode('ascii')
    return pwd_hash == stored_password


def serializer_to_json(serializer_class, list_object):
    return serializer_class(list_object, many=True).data


def get_response(success=True, message='Success', result=None, detail_code='success', status_code=status.HTTP_200_OK):
    result = {
        'success': success,
        'code': detail_code,
        'message': message,
        'result': result
    }
    return response.Response(result, status=status_code)


def get_raw_response(success=True, message='Success', result=None, detail_code='success', status_code=status.HTTP_200_OK):
    result = {
        'success': success,
        'code': detail_code,
        'message': message,
        'result': result
    }
    return JsonResponse(result, status=status_code)
