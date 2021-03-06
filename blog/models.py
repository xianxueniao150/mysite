from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import exceptions
from django.utils import timezone
from django.urls import reverse


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def get_read_num(self):
        try:
            return self.read_num.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

    def __str__(self):
        return "<Blog: %s>" % self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    class Meta:
        ordering = ['-created_time']


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING, related_name="read_num")


class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_detail_num = models.IntegerField(default=0)
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING, related_name="read_detail_num")
