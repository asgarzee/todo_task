from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    title = models.CharField(max_length=200, verbose_name='Title')
    desc = models.TextField(verbose_name='Description')

    def __unicode__(self):
        return self.title
