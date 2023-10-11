from repositories import UserdataRepository

class UserdataService():
  def __init__(self, userdata_repository: UserdataRepository) -> None:
    self.userdata_repository = userdata_repository
    pass