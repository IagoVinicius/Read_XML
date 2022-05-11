from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routes import read_xml, upload, unzip

api = FastAPI()
api.mount('/static', StaticFiles(directory='static'), name='static')

api.include_router(read_xml.router)
api.include_router(upload.router)
api.include_router(unzip.router)