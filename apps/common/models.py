import uuid

from django.db import models


class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

# Abstract base classes are useful when you want to put some common information
# into a number of other models. You write your base class and put abstract=True
# in the Meta class. This model will then not be used to create any database table.
# Instead, when it is used as a base class for other models,
# its fields will be added to those of the child class.
    class Meta:
        abstract = True
