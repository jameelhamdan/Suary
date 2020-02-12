from django.utils import timezone
import mongoengine as mongo
from _common import utils
import auth.models


class AbstractDocument(mongo.Document):
    uuid = mongo.StringField(primary_key=True, default=utils.generate_uuid)
    created_by = mongo.ReferenceField(auth.models.UserData, required=True)
    created_on = mongo.DateTimeField(default=timezone.now)
    updated_on = mongo.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        return super(AbstractDocument, self).save(*args, **kwargs)

    meta = {
        'abstract': True,
        'db_alias': 'default',
    }


class Post(AbstractDocument):
    content = mongo.StringField(min_length=3, required=True)
    media_uuid = mongo.ListField(mongo.StringField())

    meta = {
        'collection': 'posts'
    }


class Comment(AbstractDocument):
    content = mongo.StringField(min_length=3, required=True)

    meta = {
        'collection': 'comments'
    }


class Like(AbstractDocument):
    parent = mongo.GenericLazyReferenceField(choices=(Post, Comment))

    meta = {
        'collection': 'likes',
        'indexes': ['parent'],

    }
