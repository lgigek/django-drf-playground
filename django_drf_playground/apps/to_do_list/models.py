from uuid import uuid4

from django.db import models

from model_utils import Choices


class StandardModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class User(StandardModelMixin):
    name = models.CharField(max_length=50)
    identifier = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.identifier


class Task(StandardModelMixin):
    STATUS = Choices(
        # 1st value is what is saved on db, 2nd value is what is used on code, 3rd value is what displays on admin
        ("to_do", "TO_DO", "To do"),
        ("in_progress", "IN_PROGRESS", "In progress"),
        ("done", "DONE", "done"),
    )

    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
