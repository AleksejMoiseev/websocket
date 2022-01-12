import json

from fastapi import APIRouter, WebSocket, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()

router.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@router.websocket("/api/v1/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    counter = 0
    while True:
        message = await websocket.receive_text()
        counter += 1
        response_data = {
            'id': counter,
            'message': message,
        }
        await websocket.send_json(response_data)


@router.get('/')
def root(request: Request):
    context = {
        'request': request,
        'title': 'Use Websocket'
    }
    return templates.TemplateResponse('index.html', context=context)
