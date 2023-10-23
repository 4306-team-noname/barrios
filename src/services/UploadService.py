import os
import uuid
from typing import List
from typing import Dict
# from result import Result, Ok, Err
from emmett.orm import Database
from models.Upload import Upload
from utils.Result import Result

class UploadService():
    storage_dir: str = None
    accepted_filetypes: List[str] = None
    db: Database = None

    def __init__(self, db, storage_path, accepted_filetypes) -> None:
        self.db = db
        self.__init_storage_dir(storage_path)
        self.accepted_filetypes = accepted_filetypes
        pass
    

    def __init_storage_dir(self, storage_path):
        exists = os.path.isdir(storage_path)
        if not exists:
            os.mkdir(storage_path)
        self.storage_dir = storage_path
    

    def is_valid_filetype(self, ext: str):
        if len(self.accepted_filetypes) == 0:
            return True
        
        return ext in self.accepted_filetypes


    async def save_file(self, file) -> Result:
        id = str(uuid.uuid4())
        ext = file.content_type.split('/',1)[1]
        temp_file_location = f"{self.storage_dir}/{id}.{ext}"

        if not self.is_valid_filetype(ext):
            return {'ok': False, 'error': f'{ext} is not a valid file type'}
        
        await file.save(temp_file_location)
        return {'ok': True, 'value': temp_file_location}
    

    def delete_temp_file(self, file_path) -> Result[bool, str]:
        try:
            os.remove(file_path)
            return {'ok':True}
        except FileNotFoundError:
            return {'ok': False, 'error': f'No file to delete at {file_path}'}


    async def create_upload(self, file) -> Result:
        file_save_result = await self.save_file(file)
        temp_file_location = None

        match file_save_result['ok']:
            case True:
                temp_file_location = file_save_result['value']
            case False:
                return file_save_result
            
        upload = Upload.create(file_name=file.filename)
        print(f'File name: {file.filename}')

        if upload['id'] == None: # we got an error!
            error_key = list(upload['errors'])[0]
            return {'ok': False, 'error': upload['errors'][error_key]}
            
        return {'ok': True, 'value': {'id': upload['id'], 'temp_file_location': temp_file_location}}