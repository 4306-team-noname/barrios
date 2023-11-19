from django.core.validators import FileExtensionValidator
from django.db.models import (
    DateTimeField,
    FileField,
    Manager,
    Model,
)


class UploadManager(Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("upload_date")


class Upload(Model):
    file = FileField(upload_to="uploads/", validators=[FileExtensionValidator(["csv"])])
    upload_date = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "uploads"

    def __str__(self):
        return f"({self.pk}, {self.file}, {self.upload_date})"
