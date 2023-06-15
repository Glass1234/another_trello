from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app import app
from app.routes.auth import router_auth
from app.routes.board import router_board
from app.routes.boards import router_boards
from app.routes.master import router_main

app.include_router(router_main)
app.include_router(router_auth)
app.include_router(router_boards)
app.include_router(router_board)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
register_tortoise(
    app,
    db_url='postgres://{0}:{1}@{2}:{3}/{4}'.format(
        f'admin',
        f'admin',
        f'127.0.0.1',
        f'5433',
        f'admin')
    ,
    modules={'models': ['app.db.models']},
    generate_schemas=True,
    add_exception_handlers=True
)
