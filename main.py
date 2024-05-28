
from fastapi import FastAPI
app = FastAPI()

# REquest Name
@app.get("/welcome") 
def welcome():
    return{
        'message':'Hello World!'
    }

