import uuid
from django.db.models import CharField, DateTimeField, UUIDField, Manager, Model


class UploadManager(Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("upload_date")


class Upload(Model):
    file_name = CharField(max_length=200)
    file_uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_path = CharField(max_length=200)
    upload_date = DateTimeField("date uploaded")

    class Meta:
        db_table = "uploads"

    def __str__(self):
        return f"""{{
            file_name: {self.file_name},
            file_uuid: {self.file_uuid},
            file_path: {self.file_path},
        }}"""
