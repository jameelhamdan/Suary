from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from django.core import validators
import re


class UsernameValidator(object):
    def __call__(self, value):
        if not re.match(r'^[0-9a-zA-Z._]+$', value):
            message = _('Username contains illegal characters, please make sure to only user characters from the Alphabetic, numbers, dots or underscores only.')
            raise serializers.ValidationError(message)
