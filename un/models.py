from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


# Create your models here.
class Album(models.Model):
    class Meta():
        db_table = 'album'

    album_user = models.ForeignKey(User)
    album_name = models.CharField(max_length=30)
    album_description = models.CharField(max_length=200)
    album_date = models.DateTimeField()

    def __str__(self):
        return self.album_name


class Photo(models.Model):
    class Meta():
        db_table = 'photo'

    photo_user = models.ForeignKey(User)
    photo_album = models.ForeignKey(Album)
    photo_name = models.CharField(max_length=20)
    photo_description = models.CharField(max_length=100)
    photo_date = models.DateTimeField()
    photo_image = models.ImageField(upload_to='images/')

#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.photo_name

    def bit (self):
        if self.photo_image:
            return u'<img src="%s" width="70"/>'% self.photo_image.url
        else:
            return u'(none)'
    bit.short_descriptio = u'Image'
    bit.allow_tags = True