from user_service.api import crud
from user_service.api.models import UserDB, UserSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/", response_model=UserDB, status_code=201)
async def create_user(payload: UserSchema):
    user_id = await crud.post(payload)

    response_object = {
        "id": user_id,
        "username": payload.username,
        "enabled": payload.enabled
    }
    return response_object