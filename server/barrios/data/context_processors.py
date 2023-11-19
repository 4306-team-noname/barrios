from .models import Upload


def upload_count(request):
    return {"upload_count": Upload.objects.count()}
