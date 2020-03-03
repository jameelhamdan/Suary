from django.utils import timezone
from django.conf import settings
from django.db import models, transaction
from django.db.models import Q
from django.contrib.postgres.fields import JSONField
from rest_framework.exceptions import ValidationError
import users.models
from _common import utils, validators


LOG_ACTION_LOGIN = 'login'
LOG_ACTION_REGISTER = 'register'
LOG_ACTION_LOGIN_FAIL = 'fail'
LOG_ACTION_LOGOUT_ALL = 'logout_all'
LOG_ACTION_UNAUTHORIZED = 'Forbidden'

LOG_ACTIONS = (
    (LOG_ACTION_LOGIN, 'Login'),
    (LOG_ACTION_REGISTER, 'Register'),
    (LOG_ACTION_LOGIN_FAIL, 'Login Failed'),
    (LOG_ACTION_LOGOUT_ALL, 'Logout all sessions'),
    (LOG_ACTION_UNAUTHORIZED, 'Forbidden'),
)


class User(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_index=True, default=utils.generate_uuid, editable=False)
    username = models.CharField(max_length=128, unique=True, db_index=True, null=False, editable=False, validators=[validators.UsernameValidator])
    email = models.EmailField(max_length=128, unique=True, db_index=True, null=False)
    avatar_uuid = models.CharField(max_length=36, null=True)
    password_hash = models.CharField(max_length=512)
    secret_key = models.CharField(max_length=108, db_index=True, default='')
    last_login = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_data(self):
        return users.models.UserData.objects.get(pk=self.pk)

    def get_secret_key(self):
        return utils.hash_password(self.secret_key)

    def set_password(self, new_password):
        self.password_hash = utils.hash_password(new_password)
        self.save()

    def validate_password(self, password):
        return utils.verify_password(self.password_hash, password)

    def reset_secret_key(self):
        self.secret_key = utils.generate_uuid(3)
        self.save()

    @staticmethod
    def exists(username, email):
        return User.objects.filter(Q(username=username) | Q(email=email)).exists()

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()

    @staticmethod
    def create_user(username, email, password, **kwargs):
        new_user = User(username=username, email=email)
        # this is a postgre only transaction, it will *only* revert postgre changes.
        with transaction.atomic():
            new_user.secret_key = utils.generate_uuid(3)
            new_user.save()
            new_user.set_password(password)

            user_data = users.models.UserData(
                pk=new_user.pk,
                username=new_user.username,
                email=new_user.email,
                **kwargs
            )

            user_data.save()
        return new_user

    def update_avatar(self, new_avatar):
        import media.models

        # Delete Old avatar
        avatar_uuid = self.avatar_uuid
        if avatar_uuid:
            old_avatar = media.models.MediaDocument.objects.filter(pk=avatar_uuid).first()
            if old_avatar:
                old_avatar.delete()

        # Upload new avatar
        media_document = media.models.MediaDocument(parent_id=self.pk)
        media_document.upload(new_avatar)
        media_document.save()

        self.avatar_uuid = media_document.pk
        self.save()

        user_data = self.get_data()
        user_data.avatar_uuid = media_document.pk
        user_data.save()

        return media_document.pk

    def follow(self, user_pk):
        from users.models import Follow
        user_exists = User.objects.filter(pk=user_pk).exists()

        if not user_exists:
            raise ValidationError(u'User doesn\'t exist')

        follow = Follow.objects.filter(follower_id=self.pk, following_id=user_pk).first()

        if follow and follow.is_active:
            raise ValidationError(u'Already following this user')

        if follow:
            follow.is_active = True
            follow.save()

        else:
            follow = Follow(
                follower_id=self.pk,
                following_id=user_pk,
            )

            follow.save()

        return follow

    def unfollow(self, user_pk):
        from users.models import Follow
        user_exists = User.objects.filter(pk=user_pk).exists()

        if not user_exists:
            raise ValidationError(u'User doesn\'t exist')

        follow = Follow.objects.filter(follower_id=self.pk, following_id=user_pk).first()

        if not follow or not follow.is_active:
            raise ValidationError(u'Already unfollowed this user')

        if follow:
            follow.is_active = False
            follow.save()

        return follow

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = utils.generate_uuid()
            self.secret_key = utils.generate_uuid(3)

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        db = settings.DEFAULT_DATABASE


class AccessLog(models.Model):
    action = models.CharField(max_length=16, choices=LOG_ACTIONS, default=LOG_ACTION_LOGIN)
    ip = models.GenericIPAddressField(db_index=True, null=True)
    agent = models.CharField(max_length=128, null=True)
    http_accept = models.CharField(max_length=1025)
    path_info = models.CharField(max_length=255)
    data = JSONField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.ip, self.agent)

    class Meta:
        db = settings.DEFAULT_DATABASE
