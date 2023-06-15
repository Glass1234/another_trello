from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.db.models import User, Board
from app.routes.auth import check_token
from app.schemas import BoardUser

router_boards = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
JWT_SECRET = 'myjwtsecret'


@router_boards.get('/boards')
async def index(user: User = Depends(check_token)):
    all_boards = await user.boards.all()
    print("all Boards:", user.id)
    return {'boards': all_boards}


@router_boards.post('/boards')
async def index(board: BoardUser, user: User = Depends(check_token)):
    print("creat Board:", board.name, board.background_color)
    create_board = await Board(name=board.name, background_color=board.background_color)
    create_board.avtor = user
    await create_board.save()
    return {'response': 'yes', 'id': create_board.id}


#
@router_boards.put('/boards')
async def index(board: BoardUser, user: User = Depends(check_token)):
    print("edit Board:", board.name, board.background_color, board.id)
    board_edit = await Board.filter(id=board.id).first()
    if board_edit:
        board_edit.name = board.name
        board_edit.background_color = board.background_color
        await board_edit.save()
        return {'response': 'yes'}
    return {'response': 'no'}


@router_boards.delete('/boards')
async def index(board_id: int, user: User = Depends(check_token)):
    print("delete Board:", board_id)
    board = await Board.filter(id=board_id).first()
    if board:
        columns = await board.colums.all()
        if columns:
            for column in columns:  # type Column
                tasks = await column.tasks.all()
                for task in tasks:  # type Task
                    await task.delete()
                await column.delete()
        await board.delete()
        return {'response': 'yes'}
    return {'response': 'error'}
