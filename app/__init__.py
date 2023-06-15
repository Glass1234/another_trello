
from fastapi import FastAPI
import json

from starlette.staticfiles import StaticFiles


SECRET_KEY = 'admin'

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
