from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse

router_main = APIRouter()


@router_main.get('/')
async def home(request: Request):
    return {'test': 'test'}
