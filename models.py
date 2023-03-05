from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class User(BaseModel):
    # id: Optional[UUID] = uuid4()
    id: int
    username: str
    first_name: str
    last_name: str
    gender: Gender
    profile_picture: str

class Post(BaseModel):
    # id: Optional[UUID] = uuid4()
    id: int
    desc: Optional[str]
    photo: str
    date: str
    user_id: int
    like: int
    comment: int