from _common.utils import hash_password, verify_password, generate_uuid
from django.utils import timezone
from django.db import models, transaction
from django.db.models import Q
import mongoengine as mongo
from _common import utils


class User(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, db_index=True, default=utils.generate_uuid, editable=False)
    username = models.CharField(max_length=128, unique=True, db_index=True, null=False)
    email = models.EmailField(max_length=128, unique=True, db_index=True, null=False)
    avatar_url = models.TextField(null=True)

    password_hash = models.CharField(max_length=512)
    secret_key = models.CharField(max_length=108, db_index=True, default='')

    last_login = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_data(self):
        return UserData.objects.get(uuid=self.pk)

    def get_secret_key(self):
        return hash_password(self.secret_key)

    def set_password(self, new_password):
        self.password_hash = hash_password(new_password)
        self.save()

    def validate_password(self, password):
        return verify_password(self.password_hash, password)

    def reset_secret_key(self):
        self.secret_key = generate_uuid(3)
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
            new_user.secret_key = generate_uuid(3)
            new_user.save()
            new_user.set_password(password)

            user_data = UserData(
                uuid=new_user.uuid,
                username=new_user.username,
                email=new_user.email,
                **kwargs
            )

            user_data.save()
        return new_user

    def save(self, extra_data=None, *args, **kwargs):
        if not self.pk:
            self.uuid = generate_uuid()
            self.secret_key = generate_uuid(3)

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class UserData(mongo.Document):
    uuid = mongo.StringField(primary_key=True)
    created_on = mongo.DateTimeField(default=timezone.now)
    updated_on = mongo.DateTimeField(default=timezone.now)
    username = mongo.StringField(required=True)
    email = mongo.EmailField(required=True)

    full_name = mongo.StringField(required=True)
    birth_date = mongo.DateField(required=True)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        return super(UserData, self).save(*args, **kwargs)

    meta = {
        'db_alias': 'default',
    }
