from django.db import models
from django.db.models.query import QuerySet

#Abstract Query Set for further abstract method
class AbstractQuerySet(QuerySet):
    pass

#Abstract Model Manager
#Override the __init__ to add 'alive_only' argument for all child usage
class AbstractModelManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(AbstractModelManager, self).__init__(*args, **kwargs)
