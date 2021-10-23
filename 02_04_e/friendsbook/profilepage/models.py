from django.db import models
from django.db.models.deletion import CASCADE
from django.apps import apps
from useraccount.models import UserAccount
from business.models import Business

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class ProfilePage(models.Model):
    #user_account = models.ForeignKey(UserAccount, null=True, blank=False, on_delete=CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    subject = GenericForeignKey('content_type', 'object_id')
    
    #def __str__(self):
    #    return '{} {}'.format(self.content_type, self.subject.name)