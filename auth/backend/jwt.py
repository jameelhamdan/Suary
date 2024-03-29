from django.utils.functional import SimpleLazyObject
from ..backend.settings import api_settings
from datetime import datetime, timedelta
from ..models import User
import jwt


AUTH_TOKEN_EXPIRATION_PERIOD = timedelta(minutes=api_settings.AUTH_TOKEN_LIFETIME)
REFRESH_TOKEN_EXPIRATION_PERIOD = timedelta(minutes=api_settings.REFRESH_TOKEN_LIFETIME)

MAIN_SECRET_KEY = api_settings.SIGNING_KEY
ALGORITHM = api_settings.ALGORITHM
user_id_field = api_settings.USER_ID_FIELD


def get_user_by_id(user_id):
    return User.objects.get(**{user_id_field: user_id})


def get_refresh_token_secret_key(user_secret_key):
    return '{}_{}'.format(MAIN_SECRET_KEY, user_secret_key)


def get_secret_key():
    return MAIN_SECRET_KEY


def decode_token(token, verify=True):
    try:
        # Decode Token
        secret_key = get_secret_key()
        token_data = jwt.decode(token, secret_key, verify=verify, algorithms=[ALGORITHM, ])
        return token_data

    except jwt.ExpiredSignatureError:
        raise Exception('Token Expired')


def decode_refresh_token(token, user_secret_key='', verify=True):
    try:
        # Decode Token
        secret_key = get_refresh_token_secret_key(user_secret_key)
        token_data = jwt.decode(token, secret_key, verify=verify, algorithms=[ALGORITHM, ])
        return token_data

    except jwt.ExpiredSignatureError:
        raise Exception('Token Expired')


def create_auth_token(user_id):
    expire_date = datetime.utcnow() + AUTH_TOKEN_EXPIRATION_PERIOD

    # Create new auth token
    token = jwt.encode({user_id_field: user_id, 'exp': expire_date}, get_secret_key(), algorithm=ALGORITHM, )
    return token


def create_refresh_token(user_id, user_secret_key):
    expire_date = datetime.utcnow() + REFRESH_TOKEN_EXPIRATION_PERIOD

    # Create new auth token
    secret_key = get_refresh_token_secret_key(user_secret_key)
    token = jwt.encode({user_id_field: user_id, 'exp': expire_date}, secret_key, algorithm=ALGORITHM, )
    return token


def verify_auth_token(token):
    try:

        # Validate and Decode Token
        decoded_token = decode_token(token)
        user_id = decoded_token[user_id_field]
        lazy_user = SimpleLazyObject(lambda: get_user_by_id(user_id))
        return lazy_user

    except User.DoesNotExist:
        raise Exception('This User Doesn\'t Exist!')

    except jwt.ExpiredSignatureError:
        raise Exception('This Token is expired!')


def verify_refresh_token(token):
    try:

        # Validate and Decode Token
        try:
            user_id = decode_token(token, verify=False)[user_id_field]
        except KeyError:
            raise Exception('Invalid Token')
        user = get_user_by_id(user_id)

        decode_refresh_token(token, user.get_secret_key())

        return user

    except User.DoesNotExist:
        raise Exception('This User Doesn\'t Exist!')

    except jwt.ExpiredSignatureError:
        raise Exception('This Token is expired!')


def renew_refresh_token(token, user_secret_key):
    token = decode_refresh_token(token, user_secret_key)
    user_id = token[user_id_field]
    expiration_date = token['exp']
    # Renew refresh token if is about to expire otherwise return same token
    if datetime.utcnow() - timedelta(microseconds=expiration_date) > datetime.utcnow() - timedelta(hours=1):
        return create_refresh_token(user_id, user_secret_key)
    else:
        return token
