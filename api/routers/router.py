from fastapi import APIRouter,HTTPException,Depends
from datetime import datetime
import time
from fastapi import BackgroundTasks,Depends

router = APIRouter(
    prefix="/api",
    tags=["transaction"]
)

@router.get("/")
async def check_transaction():
    return {"message": "Hello World"}