import os
from uuid import uuid4
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from askdjango.utils import thumbnail


def validator_even_length(s):
    if len(s) % 2 != 0:
        raise ValidationError('짝수길이로 입력하세요.')

def random_name_upload_to(instance, filename):
    ext = os.path.splitext(filename)[-1].lower()
    name = uuid4().hex
    return name[:2] + '/' + name[2:4] + '/' + name[4:] + ext

class Post(models.Model):
    title = models.CharField(max_length=100, validators=[validator_even_length])
    content = models.TextField()
    photo = models.ImageField(blank=True,
        # upload_to='hello/world/%Y'
        upload_to=random_name_upload_to
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return '/blog/posts/%d/' % self.id
        # return reverse('blog:post_detail', args=[self.pk])
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    # https://docs.djangoproject.com/en/1.9/ref/signals/#django.db.models.signals.pre_save
    @staticmethod
    def on_pre_save(sender, **kwargs):
        post = kwargs['instance']
        if post.photo:
            max_width = 600
            if post.photo.width > max_width or post.photo.height > max_width:
                thumbnail_file = thumbnail(post.photo.file, max_width, max_width)
                post.photo.save(post.photo.name, File(thumbnail_file))

pre_save.connect(Post.on_pre_save, sender=Post)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)

