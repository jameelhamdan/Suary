from django.conf import settings
from rest_framework.exceptions import ValidationError
import djongo.models as mongo
from _common import utils
import users.models
from django import forms


class AbstractDocument(mongo.Model):
    id = mongo.CharField(max_length=36, db_column='_id', primary_key=True, default=utils.generate_uuid)
    created_by = mongo.ForeignKey(users.models.UserData, on_delete=mongo.CASCADE, null=False)
    created_on = mongo.DateTimeField(auto_now_add=True)
    updated_on = mongo.DateTimeField(auto_now=True)

    objects = mongo.DjongoManager()

    class Meta:
        abstract = True


class PostMedia(mongo.Model):
    hash = mongo.TextField()
    content_type = mongo.TextField()

    class Meta:
        abstract = True


class PostMediaForm(forms.ModelForm):
    class Meta:
        model = PostMedia
        fields = ('hash', 'content_type', )


class Post(AbstractDocument):
    content = mongo.TextField(null=False)
    tags = mongo.ListField(mongo.CharField(), default=[])
    media_list = mongo.ListField(
        mongo.EmbeddedField(
            model_container=PostMedia,
            model_form_class=PostMediaForm
        ), default=[]
    )

    def add_comment(self, content, created_by):
        comment = Comment(post_id=self.pk, content=content, created_by_id=created_by.pk)
        comment.save()

        return comment

    def add_like(self, user_pk):
        user_exists = users.models.UserData.objects.filter(pk=user_pk).exists()

        if not user_exists:
            raise ValidationError(u'User doesn\'t exist')

        like = Like.objects.filter(post_id=self.pk, created_by_id=user_pk).first()

        if like:
            raise ValidationError(u'Already liked this post')

        else:
            like = Like(
                post_id=self.pk,
                created_by_id=user_pk,
            )
            like.save()

        return like

    def remove_like(self, user_pk):
        user_exists = users.models.UserData.objects.filter(pk=user_pk).exists()

        if not user_exists:
            raise ValidationError(u'User doesn\'t exist')

        like = Like.objects.filter(post_id=self.pk, created_by_id=user_pk).first()

        if not like:
            raise ValidationError(u'Already not liking this post')

        else:
            like.delete()

        return None

    def get_likes_count(self):
        return self.likes.count()

    def get_comments_count(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if self.content:
            self.tags = [i for i in self.content.split() if i.startswith("#")]

        super(Post, self).save(*args, **kwargs)

    class Meta:
        db_table = 'main_posts'
        db = settings.MONGO_DATABASE


class Comment(AbstractDocument):
    post = mongo.ForeignKey(Post, on_delete=mongo.CASCADE, related_name='comments', null=False)
    content = mongo.TextField(null=False)

    class Meta:
        db_table = 'main_comments'
        db = settings.MONGO_DATABASE


class Like(AbstractDocument):
    post = mongo.ForeignKey(Post, on_delete=mongo.CASCADE, related_name='likes', null=True)
    comment = mongo.ForeignKey(Comment, on_delete=mongo.CASCADE, related_name='likes', null=True)

    class Meta:
        db_table = 'main_likes'
        db = settings.MONGO_DATABASE
