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
    file = FileField(upload_to="uploads/")
    upload_date = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "uploads"
