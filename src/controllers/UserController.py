from ..services.UserService import UserService

class UserController():
  def __init__(self, user_service: UserService) -> None:
    self.user_service = user_service
    pass