from django.db import models
from core.models import AbstractModel
from django.conf import settings
from .managers import BugManager

# Create your models here.
class Bug(AbstractModel):
    title = models.CharField(max_length=50) # title
    desc = models.CharField(max_length=200) # full description
    is_open = models.BooleanField(default=True) # flag to control the bug is open or close
    handle_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # current handled user

    objects = BugManager() # return only the is_open=true
    all_objects = BugManager(alive_only=False) # return all for admin purpose

    def __str__(self):
        return f'{self.title} handle by {self.handle_by}'

