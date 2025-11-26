from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from models.User import User

router = APIRouter()
templates = Jinja2Templates("/templates/users")


@router.get("/user/{user_id}", response_class=HTMLResponse)
def get_user(request: Request, user_id: int):

    return templates.TemplateResponse("detail_user.html", { "request": request, })


@router.get("/create_user", response_class=HTMLResponse)
def get_form_create_user(request: Request):
    return templates.TemplateResponse("create_user.html", { "request": request })


@router.post("/create_user", response_class=HTMLResponse)
def create_user(user: User):
    print(f'name: {user.name} - age: {user.age} - friends: {user.friends}' )