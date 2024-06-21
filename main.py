import os
import django


# Set the default settings module for the Django environment

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogApplication.settings")
# Initialize Django

django.setup()

from fastapi import FastAPI,Request
from myapp.router import router


app = FastAPI()


# Include API routes
app.include_router(router)

@app.get("/")
async def root():
    return{"message":"use this url for testing json output in swagger http://127.0.0.1:8000/docs"}
