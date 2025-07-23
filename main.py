from fastapi import FastAPI
from api import router as car_router

app = FastAPI()
app.include_router(car_router)
