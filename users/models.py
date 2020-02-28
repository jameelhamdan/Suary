from django.conf import settings
import djongo.models as mongo
from _common import utils


class Follow(mongo.Model):
    id = mongo.CharField(max_length=36, db_column='_id', primary_key=True, default=utils.generate_uuid)
    created_on = mongo.DateTimeField(auto_now_add=True)
    updated_on = mongo.DateTimeField(auto_now=True)
    is_blocked = mongo.BooleanField(default=False)
    is_active = mongo.BooleanField(default=True)
    follower = mongo.ForeignKey('UserData', related_name='following', on_delete=mongo.CASCADE, null=False)
    following = mongo.ForeignKey('UserData', related_name='followers', on_delete=mongo.CASCADE, null=False)

    objects = mongo.DjongoManager()

    class Meta:
        db_table = 'users_follow'
        db = settings.MONGO_DATABASE
        unique_together = ['follower', 'following']


class UserData(mongo.Model):
    id = mongo.CharField(max_length=36, db_column='_id', primary_key=True)
    created_on = mongo.DateTimeField(auto_now_add=True)
    updated_on = mongo.DateTimeField(auto_now=True)
    username = mongo.CharField(max_length=36, db_index=True, unique=True, null=False)
    email = mongo.EmailField(max_length=36, db_index=True, unique=True, null=False)

    avatar_uuid = mongo.CharField(max_length=36)
    full_name = mongo.CharField(max_length=256, null=False)
    birth_date = mongo.DateField(null=False)

    objects = mongo.DjongoManager()

    class Meta:
        db_table = 'user_data'
        db = settings.MONGO_DATABASE
        unique_together = ['username', 'email']
