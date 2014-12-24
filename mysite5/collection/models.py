from django.db import models
from django.contrib.auth.models import User
from WebPage.models import webpage

class user_behavior(models.Model):
    def __unicode__(self):
        return self.user

    user = models.ForeignKey(User)
    link = models.ForeignKey(webpage)
    time = models.DateTimeField()
