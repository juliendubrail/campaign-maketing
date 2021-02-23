from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    enabled: bool

class UserDB(UserSchema):
    id: int

