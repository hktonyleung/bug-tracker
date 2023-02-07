from core.managers import AbstractModelManager

# Custom bug manager to override existing methold or add extra methods
class BugManager(AbstractModelManager):

    # return queryset filter by is_open
    def get_queryset(self):
        if self.alive_only:
            return super().get_queryset().filter(is_open=True)
        return super().get_queryset()