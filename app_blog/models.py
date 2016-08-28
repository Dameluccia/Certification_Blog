from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

def upload_location(instance,filename):
    return "%s/%s" % (instance.slug, filename)


class Post(models.Model):
    title = models.CharField(unique=True, max_length=120)
    slug = AutoSlugField(null=True, populate_from = "title")
    image = models.ImageField(upload_to=upload_location,
    null=True, blank=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish= models.DateField(auto_now=False, auto_now_add= False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)




    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug' : self.slug})
    def get_absolute_url_bis(self):
        return reverse('draft_detail', kwargs={'slug' : self.slug})
