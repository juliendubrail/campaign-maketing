from user_service.api.models import UserSchema
from user_service.db import users, database

async def post(payload: UserSchema):
   query = users.insert().values(username=payload.username, enabled=payload.enabled)
   return await database.execute(query=query)