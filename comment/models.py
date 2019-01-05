from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING, related_name="comment")
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="comment")

    root = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, related_name='root_comment')
    parent = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, related_name="parent_comment")
    reply_to = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name="reply")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-comment_time", ]


