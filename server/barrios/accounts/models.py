from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, Model, OneToOneField


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Profile(Model):
    user = OneToOneField(CustomUser, on_delete=CASCADE)
