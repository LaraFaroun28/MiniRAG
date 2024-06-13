#For Dataa Logic operations
from .BaseController import BaseController
from fastapi import   UploadFile
from models import ResponseSignal
from .ProjectController import ProjectController
import re
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 

    def validate_uploaded_file(self, file:UploadFile):

        if file.content_type  not in self.app_settings.FILE_ALLOWD_TYPES:
            return False , ResponseSignal.FTLE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE*self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXEEDED.value
        
        return True , ResponseSignal.FILE_UPLOAD_SUCCESS.value
    
    def generate_unique_filepath (self , original_filename:str,prject_id:str):

        random_key = self.generatr_random_string(length=12)
        
        project_path = ProjectController().get_project_path(project_id= prject_id)

        clean_file_name = self.get_clean_filename(orginal_filenama= original_filename)

        new_file_path = os.path.join (project_path, random_key+"_"+clean_file_name)

        while os.path.exists(new_file_path):
            random_key = self.generatr_random_string()
            new_file_path = os.path.join (project_path, random_key+"_"+clean_file_name)

        return new_file_path , random_key+"_"+clean_file_name
    
    def get_clean_filename(self , orginal_filenama:str):
        
        #remove any spicial characters except underscore and.
        cleaned_filename = re.sub(r'[^\w.]','',orginal_filenama)
        
        #replace_spaces with underscore
        cleaned_filename = cleaned_filename.replace(' ' ,'_')

        return cleaned_filename


        