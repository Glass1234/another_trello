from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.db.models import User, Board, Colum, Task
from app.routes.auth import check_token
from app.schemas import TaskUser

router_board = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
JWT_SECRET = 'myjwtsecret'


@router_board.get('/board')
async def index(user: User = Depends(check_token)):
    all_boards = await user.boards.all()
    all_boards_serialized = []
    for board in all_boards:
        all_boards_serialized.append({"name": board.name,
                                      "id": board.id})
    print("all Boards:", user.id)
    return {'boards': all_boards_serialized}


@router_board.post('/board')
async def index(board_id: int, user: User = Depends(check_token)):
    board = await user.boards.filter(id=board_id).first()
    board_columns = await board.colums.all()
    tasks = []
    for column in board_columns:  # type: Colum
        tasks.append(await column.tasks.all())
    print("get board:", user.id)
    return {'board': board,
            'columns': board_columns,
            'tasks': tasks}


@router_board.post('/createColum')
async def index(colum_name: str, board_id: int, user: User = Depends(check_token)):
    print("create colum:", user.id)
    board = await Board.filter(id=board_id).first()
    if board:
        col = Colum(name=colum_name, board=board)
        await col.save()
        col = col.id
        return {'response': "yes", "column_id": col}
    return {'response': "error"}


@router_board.delete('/colum')
async def index(column_id: int, board_id: int, user: User = Depends(check_token)):
    print("delete column:", user.id)
    board = await Board.filter(id=board_id).first()
    if board:
        column = await Colum.filter(id=column_id).first()
        if column:
            tasks = await column.tasks.all()
            for task in tasks:  # type: Task
                await task.delete()
        await column.delete()
        return {'response': "yes"}
    return {'response': "error"}


@router_board.post('/task')
async def index(board_id: int, column_id: int, msg: str, user: User = Depends(check_token)):
    print("create task:", user.id)
    board = await Board.filter(id=board_id).first()
    if board:
        colum = await board.colums.filter(id=column_id).first()
        if colum:
            task = Task(msg=msg, colum=colum)
            await task.save()
            return {'response': "yes", "task_id": task.id}
    return {'response': "error"}


@router_board.delete('/task')
async def index(task_id: int, user: User = Depends(check_token)):
    print("delete task:", user.id)
    task = await Task.filter(id=task_id).delete()
    if task:
        return {'response': "yes"}
    return {'response': "error"}


@router_board.put('/task')
async def index(task: TaskUser, user: User = Depends(check_token)):
    print("put Board:", task.msg, task.id)
    task_edit = await Task.filter(id=task.id).first()
    if task_edit:
        task_edit.msg = task.msg
        await task_edit.save()
        return {'response': 'yes'}
    return {'response': 'no'}
