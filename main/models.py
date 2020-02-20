from django.utils import timezone
from django.conf import settings
import djongo.models as mongo
from _common import utils
import auth.models


class AbstractDocument(mongo.Model):
    id = mongo.CharField(max_length=36, primary_key=True, default=utils.generate_uuid)
    created_by = mongo.ForeignKey(auth.models.UserData, on_delete=mongo.CASCADE, null=False)
    created_on = mongo.DateTimeField(auto_now_add=True)
    updated_on = mongo.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        return super(AbstractDocument, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        db = settings.MONGO_DATABASE


class Post(AbstractDocument):
    content = mongo.TextField(null=False)
    media_list = mongo.ListField(mongo.CharField(), default=[])

    def add_comment(self, content, created_by):
        comment = Comment(post_id=self.pk, content=content, created_by=created_by)
        comment.save()

        return comment

    class Meta:
        db_table = 'main_posts'


class Comment(AbstractDocument):
    post = mongo.ForeignKey(Post, on_delete=mongo.CASCADE, null=False)
    content = mongo.TextField(null=False)

    class Meta:
        db_table = 'main_comments'


class Like(AbstractDocument):
    post = mongo.ForeignKey(Post, on_delete=mongo.CASCADE, null=True)
    comment = mongo.ForeignKey(Comment, on_delete=mongo.CASCADE, null=True)

    class Meta:
        db_table = 'main_likes'
