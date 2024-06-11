from helpers.config import get_settings , Settings
import os
import random
import string
class BaseController:
    def __init__(self):
         self.app_settings = get_settings()
         #get path to current file, then peth to directory (controller), so it returns path
         #to controller dir
         self.base_dir = os.path.dirname(os.path.dirname(__file__))
         #Get to --> assets--> files
         self.file_dir = os.path.join(self.base_dir , "assets/files")

    def generatr_random_string(self , length:int):
         return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        
