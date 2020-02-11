from django.utils import timezone
import mongoengine as mongo
import uuid


class AbstractDocument(mongo.Document):
    uuid = mongo.UUIDField(unique=True, binary=False, default=uuid.uuid4)
    created_by = mongo.UUIDField(binary=False, required=True)
    created_on = mongo.DateTimeField(default=timezone.now())
    updated_on = mongo.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        return super(AbstractDocument, self).save(*args, **kwargs)

    meta = {
        'allow_inheritance': True,
        'indexes': ['uuid'],
        'db_alias': 'default',
    }


class Post(AbstractDocument):
    content = mongo.StringField(min_length=3, required=True)
    image_uuid = mongo.ListField(mongo.StringField())

    meta = {
        'collection': 'posts'
    }


class Comment(AbstractDocument):
    content = mongo.StringField(min_length=3, required=True)

    meta = {
        'collection': 'posts'
    }


class Like(AbstractDocument):
    parent = mongo.GenericLazyReferenceField(choices=(Post, Comment))

    meta = {
        'collection': 'likes',
        'indexes': ['uuid', 'parent'],

    }
