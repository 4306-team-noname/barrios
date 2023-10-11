from services import FileService
from services import UserdataService
class UserDataController():
  def __init__(self, userdata_service: UserdataService, file_service: FileService) -> None:
    self.userdata_service = userdata_service
    self.file_service = file_service
    pass