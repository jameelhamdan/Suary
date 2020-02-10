from _common.utils import hash_password, verify_password, generate_uuid
from django.utils import timezone
from django.db import models
from django.db.models import Q
import uuid
DEFAULT_PAGE_SIZE = 10


class User(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=128, unique=True, db_index=True, null=False)
    email = models.EmailField(max_length=128, unique=True, db_index=True, null=False)
    avatar_url = models.TextField(null=True)

    password_hash = models.CharField(max_length=512)
    secret_key = models.CharField(max_length=108, db_index=True, default='')

    last_login = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def set_password(self, new_password):
        self.password_hash = hash_password(new_password)
        self.save()

    def validate_password(self, password):
        return verify_password(self.password_hash, password)

    def reset_secret_key(self):
        self.secret_key = generate_uuid(3)
        self.save()

    @staticmethod
    def exists(user_name, email):
        return User.objects.filter(Q(user_name=user_name) | Q(email=email)).exists()

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()

    @staticmethod
    def create_user(user_name, email, password):
        new_user = User(user_name=user_name, email=email)
        new_user.save()
        new_user.set_password(password)
        return new_user

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = generate_uuid()
            self.secret_key = generate_uuid(3)
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_name
