from fastapi import Depends, FastAPI, HTTPException

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

# global dependency
# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# Dependency injection

# Dependency
async def check_name(name: str):
    if len(name) > 4:
        return name
    raise HTTPException(401, 'Length of name must grater than 4')


@app.get('/phone')
async def get_phone(name=Depends(check_name)):
    return {'name': name}


@app.get('/user')
async def get_user(name=Depends(check_name)):
    return {'name': name}


# sub-dependency
async def check_price(price: int, name: str = Depends(check_name)):
    if price > 50:
        return {'name': name, 'price': price}
    raise HTTPException(401, "Price must grater than 50")


@app.get('/phone/iphone')
async def get_iphone(common: dict = Depends(check_price)):
    return common
