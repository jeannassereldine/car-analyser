from fastapi import FastAPI
from routers.analyse_router import router 

app = FastAPI()
app.include_router(router)
