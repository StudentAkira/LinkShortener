from django.contrib.auth.models import AbstractUser
from django.db import models
from short_url import encode_url


# Create your models here.
class CustomUser(AbstractUser):
    pass


class ShortedLink(models.Model):
    long_url = models.URLField(default=None)
    short_url = models.URLField(default=None)
    users = models.ManyToManyField(CustomUser, blank=True)

    def cut(self, urlid):
        self.short_url = 'http://shorted_url/'+encode_url(urlid)
