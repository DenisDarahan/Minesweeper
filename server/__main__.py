import uvicorn

from server.settings import settings


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=settings.host,
        port=settings.port,
        reload=True
    )
