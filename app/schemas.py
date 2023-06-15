from pydantic import typing, validator, constr
from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator


class ClientUser(BaseModel):
    user_name: str
    passwd: str
    id: int


class BoardUser(BaseModel):
    name: typing.Optional[str]
    background_color: typing.Optional[str]

    id: typing.Optional[int]


class TaskUser(BaseModel):
    id: int
    msg: str
