from fastapi import FastAPI
from src.man.routes.users_routes import users_routes

app = FastAPI()
app.include_router(users_routes)
