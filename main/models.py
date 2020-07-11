from django.conf import settings
from rest_framework.exceptions import ValidationError
from django.db import models
from django.contrib.postgres.fields import ArrayField
from _common import utils
import auth.models
import media.models


class AbstractModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=utils.generate_uuid)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Media(models.Model):
    hash = models.TextField(db_index=True)
    content_type = models.TextField(db_index=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='media', null=True)
    comment = models.OneToOneField('Comment', on_delete=models.CASCADE, related_name='media', null=True)

    class Meta:
        db_table = 'main_media'
        db = settings.DEFAULT_DATABASE


class PostManager(models.Manager):
    def liked(self, user=None):
        return super().get_queryset().annotate(
            likes_count=models.Count('likes', distinct=True),
            comments_count=models.Count('comments', distinct=True),
            is_liked=models.Exists(
                Like.objects.filter(post_id=models.OuterRef('pk'), created_by_id=user.pk)
            )
        )


class Post(AbstractModel):
    content = models.TextField(null=False)
    tags = ArrayField(base_field=models.TextField())
    created_by = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    objects = PostManager()

    def add_comment(self, content, created_by, media_file=None):
        comment = Comment(post_id=self.pk, content=content, created_by_id=created_by.pk)
        comment.save()

        if media_file:
            media_document = media.models.MediaDocument(
                parent_id=self.pk,
                parent_type=media.models.MediaDocument.ParentTypes.COMMENT
            )
            media_document.upload(media_file)

            Media(
                comment_id=comment.pk,
                hash=media_document.pk,
                content_type=media_document.content_type
            ).save()

        return comment

    def add_like(self, user_pk):
        user_exists = auth.models.User.objects.filter(pk=user_pk).exists()

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
        user_exists = auth.models.User.objects.filter(pk=user_pk).exists()

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
        return self.comments.count()

    def save(self, *args, **kwargs):
        if self.content:
            self.tags = [i for i in self.content.split() if i.startswith("#")]

        super(Post, self).save(*args, **kwargs)

    class Meta:
        db_table = 'main_posts'
        db = settings.DEFAULT_DATABASE


class Comment(AbstractModel):
    content = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=False)
    created_by = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'main_comments'
        db = settings.DEFAULT_DATABASE


class Like(AbstractModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', null=True)
    created_by = models.ForeignKey('auth.User', related_name='likes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'main_likes'
        db = settings.DEFAULT_DATABASE
