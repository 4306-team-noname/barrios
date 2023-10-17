from emmett.tools.auth import AuthUser
from emmett.orm import has_many

class User(AuthUser):
    has_many('uploads')