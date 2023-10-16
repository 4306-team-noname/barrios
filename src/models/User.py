from emmett.tools.auth import AuthUser
from emmett.orm import has_many

class User(AuthUser):
    has_many('uploads')
    # has_many('forecasts')
    # has_many('optimizations')
    # has_many('accuracies')