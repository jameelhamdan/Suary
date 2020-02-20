from django.utils import timezone
import djongo.models as mongo
from _common import utils
import auth.models


class Follow(mongo.Model):
    id = mongo.CharField(max_length=36, primary_key=True, default=utils.generate_uuid)
    created_on = mongo.DateTimeField(auto_now_add=True)
    updated_on = mongo.DateTimeField(auto_now=True)
    is_blocked = mongo.BooleanField(default=False)
    is_active = mongo.BooleanField(default=True)
    follower = mongo.ForeignKey(auth.models.UserData, related_name='following', on_delete=mongo.CASCADE, null=False)
    following = mongo.ForeignKey(auth.models.UserData, related_name='followers', on_delete=mongo.CASCADE, null=False)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        return super(Follow, self).save(*args, **kwargs)

    class Meta:
        db_table = 'users_follow'
        unique_together = ['follower', 'following']
