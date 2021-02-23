from fastapi import FastAPI

from user_service.api import users, ping
from user_service.db import engine, metadata, database

metadata.create_all(engine)

user_service = FastAPI()

@user_service.on_event("startup")
async def startup():
    await database.connect()

@user_service.on_event("shutdown")
async def shutdown():
    await database.connect()

user_service.include_router(ping.router)
user_service.include_router(users.router, prefix="/users", tags=["users"])