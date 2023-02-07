from django.db import models
from .managers import AbstractModelManager
from django.conf import settings

# Create abstract model to group the common fields here
class AbstractModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(class)s_created_by")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(class)s_updated_by")

    class Meta:
        abstract = True

    objects = AbstractModelManager()