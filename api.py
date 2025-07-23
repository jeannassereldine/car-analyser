from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from models import Car
from services import analyze_car_image

router = APIRouter()

@router.post("/analyze-car", response_model=Car)
async def analyze_car(image: UploadFile = File(...)):
    car_info = await analyze_car_image(image)
    return JSONResponse(content=car_info.dict())
