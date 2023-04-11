from fastapi import FastAPI


app = FastAPI()


@app.get('/index/')
async def root():
    return {"message": "Hello Index"}


# @app.post('/create-user/')
# async def create_user():
#     pass
