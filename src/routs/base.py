#BASE ROUTS
#We use Base Rout .get('/') for health check, if the app is working or not.
from fastapi import FastAPI , APIRouter
import os

base_router = APIRouter(
    prefix = "/api/v1",
    tags = ["api_v1"]
)

@base_router.get("/") 
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        'message':'Hello ALL!',
        'app_name':app_name,
        'app_version':app_version
    }