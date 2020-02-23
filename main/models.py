from django.conf import settings
import djongo.models as mongo
from _common import utils
import users.models


class AbstractDocument(mongo.Model):
    id = mongo.CharField(max_length=36, db_column='_id', primary_key=True, default=utils.generate_uuid)
    created_by = mongo.ForeignKey(users.models.UserData, on_delete=mongo.CASCADE, null=False)
    created_on = mongo.DateTimeField(auto_now_add=True)
    updated_on = mongo.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(AbstractDocument):
    content = mongo.TextField(null=False)
    tags = mongo.ListField(mongo.CharField(), default=[])
    media_list = mongo.ListField(mongo.CharField(), default=[])

    def add_comment(self, content, created_by):
        comment = Comment(post_id=self.pk, content=content, created_by_id=created_by.pk)
        comment.save()

        return comment

    def save(self, *args, **kwargs):
        if self.content:
            self.tags = [i for i in self.content.split() if i.startswith("#")]

        super(Post, self).save(*args, **kwargs)

    class Meta:
        db_table = 'main_posts'
        db = settings.MONGO_DATABASE


class Comment(AbstractDocument):
    post = mongo.ForeignKey(Post, on_delete=mongo.CASCADE, null=False)
    content = mongo.TextField(null=False)

    class Meta:
        db_table = 'main_comments'
        db = settings.MONGO_DATABASE


class Like(AbstractDocument):
    post = mongo.ForeignKey(Post, on_delete=mongo.CASCADE, null=True)
    comment = mongo.ForeignKey(Comment, on_delete=mongo.CASCADE, null=True)

    class Meta:
        db_table = 'main_likes'
        db = settings.MONGO_DATABASE
