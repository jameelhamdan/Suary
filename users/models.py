from django.conf import settings
from django.db import models
from _common import utils


class Follow(models.Model):
    id = models.CharField(max_length=36, db_column='_id', primary_key=True, default=utils.generate_uuid)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    follower = models.ForeignKey('auth.User', related_name='following', on_delete=models.CASCADE, null=False)
    following = models.ForeignKey('auth.User', related_name='followers', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'users_follow'
        db = settings.DEFAULT_DATABASE
        unique_together = ['follower', 'following']
