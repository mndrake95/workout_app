from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Workout
from app.schemas import WorkoutCreate, WorkoutRead

router = APIRouter()

@router.post("/", response_model=WorkoutRead)
async def create_workout(
    workout_data: WorkoutCreate,
    db: AsyncSession = Depends(get_db)
):
    new_workout = Workout(**workout_data.model_dump(), owner_id=1)
    db.add(new_workout)
    await db.commit()
    await db.refresh(new_workout)
    return new_workout

@router.get("/", response_model=list[WorkoutRead])
async def read_workout(
    db: AsyncSession = Depends(get_db)
):
    query = select(Workout)
    result = await db.execute(query)
    return result.scalars().all()