from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32)
    passwd = fields.TextField()
    boards: fields.ReverseRelation['models.Board']
    member_boards = fields.ManyToManyField('models.Board', related_name='members', through='users_boards')


class Task(Model):
    id = fields.IntField(pk=True, index=True)
    msg = fields.TextField()
    colum = fields.ForeignKeyField('models.Colum', related_name='tasks')


class Colum(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    tasks: fields.ReverseRelation["Task"]
    board = fields.ForeignKeyField('models.Board', related_name='colums')


class Board(Model):
    id = fields.IntField(pk=True)
    avtor = fields.ForeignKeyField('models.User', related_name='boards')
    members: fields.ManyToManyRelation["User"]
    name = fields.CharField(max_length=32)
    background_color = fields.CharField(max_length=16)
    colums: fields.ReverseRelation["Colum"]
