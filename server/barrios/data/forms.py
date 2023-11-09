from django.forms import FileField, Form


class UploadFileForm(Form):
    file = FileField()
