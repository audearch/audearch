from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI(
    title='auderch',
    description='auderch is a audio fingerprinting system',
    version='0.0'
)

templates = Jinja2Templates(directory="web/templates")
jinja_env = templates.env


def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
