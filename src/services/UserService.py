from repositories import UserRepository

class UserService():
  def __init__(self, user_repository: UserRepository) -> None:
    self.user_repository = user_repository
    pass