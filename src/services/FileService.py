from repositories import FileRepository

class FileService():
  def __init__(self, file_repository: FileRepository) -> None:
    self.file_repository = file_repository
    pass