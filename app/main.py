from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from models.Number import Numbers
from models.User import User
from database import engine, Base


app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/calculate', response_class=HTMLResponse)
async def calculator(request: Request):
    return templates.TemplateResponse('calculator.html', {'request': request})


@app.post('/calculate')
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    data = {'result': result}
    return JSONResponse(content=data)
