from django.utils import timezone
import mongoengine as mongo
from _common import utils
import auth.models


class Follow(mongo.Document):
    uuid = mongo.StringField(primary_key=True, default=utils.generate_uuid)
    created_on = mongo.DateTimeField(default=timezone.now)
    updated_on = mongo.DateTimeField(default=timezone.now)
    is_blocked = mongo.BooleanField(default=False)
    is_active = mongo.BooleanField(default=True)
    follower = mongo.ReferenceField(auth.models.UserData, required=True)
    following = mongo.ReferenceField(auth.models.UserData, required=True)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        return super(Follow, self).save(*args, **kwargs)

    meta = {
        'db_alias': 'default',
        'collection': 'users_follow',
        'indexes': [
            {'fields': ('follower', 'following'), 'unique': True}
        ],
        'auto_create_index': True
    }
