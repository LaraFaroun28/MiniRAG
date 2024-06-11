from pydantic_settings import BaseSettings,SettingsConfigDict

#if we want to change the way we load data from .env we update it from settings class
class Settings(BaseSettings):

    APP_NAME : str
    APP_VERSION : str
    
    FILE_ALLOWD_TYPES : list
    FILE_MAX_SIZE : int
    FILE_DEFULT_CHUNCK_SIZE : int
    

    class Config:
        env_file= ".env"

def get_settings():
    return Settings()
