import uuid

from django.db import models

from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """
    Base model

    :cvar id: UUIDField, UUIDField, UUIDField primary key
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
