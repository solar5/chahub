import uuid

from django.conf import settings
from django.db import models

from settings.base import BundleStorage
from utils.data import PathWrapper


class Data(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_when = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=64, default="")
    description = models.TextField(null=True, blank=True)
    data_file = models.FileField(
        upload_to=PathWrapper('dataset_data_file'),
        storage=BundleStorage,
    )
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    is_public = models.BooleanField(default=False)


class DataGroup(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_when = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    datas = models.ManyToManyField(Data, related_name="groups")
