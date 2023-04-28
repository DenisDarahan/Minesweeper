from fastapi import FastAPI

from server.api import router


app = FastAPI(title='Minesweeper')
app.include_router(router)


@app.get('/')
async def ping() -> dict:
    return {'ping': 'pong'}
