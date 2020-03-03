from auth.models import AccessLog, LOG_ACTIONS, LOG_ACTION_LOGIN, LOG_ACTION_LOGIN_FAIL, LOG_ACTION_LOGOUT_ALL, LOG_ACTION_REGISTER, LOG_ACTION_UNAUTHORIZED


def _secure_items(obj):
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = _secure_items(v)
        elif not all(k.lower().find(sk) == -1 for sk in ['pass', 'password', 'key', 'secret', 'token', 'auth', 'access']):
            obj[k] = u'<REDACTED>'

    return obj


def get_request_data(request):
    # Get data from request based on method name
    data = getattr(request, request.method.upper(), {})

    data = _secure_items(data.dict())
    return data


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def log_action(request, action=LOG_ACTION_LOGIN, with_data=True):
    assert action in [a[0] for a in LOG_ACTIONS], 'Log Action not defined'

    log = AccessLog(
        ip=get_client_ip(request),
        agent=request.META.get('HTTP_USER_AGENT', '<unknown>'),
        http_accept=request.META.get('HTTP_ACCEPT', '<unknown>'),
        path_info=request.META.get('PATH_INFO', '<unknown>'),
        action=action
    )

    if with_data:
        log.data = get_request_data(request)

    log.save()
