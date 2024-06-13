from fastapi import FastAPI , APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
import aiofiles
from models import ResponseSignal
import logging

logger =logging.getLogger("uvicorn.error")

data_router = APIRouter(
    prefix = "/api/v1/data",
    tags = ["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str ,file:UploadFile,
                      app_settings:Settings = Depends(get_settings)):
    #validate the file (Logic operation)
    data_controller = DataController()
    is_valid , result_signal  = data_controller.validate_uploaded_file(file = file)

    # return {
    #     "Valid" : is_valid ,
    #         "signal" :result_signal}

    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                'signal' : result_signal
            }
        )
        


    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    #Return File_id to know which file should be processed 
    file_path , file_id = data_controller.generate_unique_filepath(original_filename= file.filename ,prject_id= project_id)

    #Open for binary writing
    try:
        async with aiofiles.open(file_path , "wb") as f:
            while chunck := await file.read(app_settings.FILE_DEFULT_CHUNCK_SIZE):
                await f.write(chunck)
    except Exception as e:
        #To know the exception, do not sent it with the response, use log file instead
        logger.error(f"Error while uploading file {e}")
        
        return JSONResponse(
        status_code = status.HTTP_400_BAD_REQUEST,
        content = {
            'signal' : ResponseSignal.FILE_UPLOAD_FAILD.value
        })
                
    
    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content = {
            'signal' : ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id" : file_id
        })
    