from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Workout, WorkoutSets
from app.schemas import WorkoutSetCreate, WorkoutSetRead
import uuid

router = APIRouter()

@router.post("/{workout_id}/sets", response_model=WorkoutSetRead)
async def create_workout_set(
    workout_id: uuid.UUID,
    workout_set_data: WorkoutSetCreate,
    db: AsyncSession = Depends(get_db)
):
    new_workout_set = WorkoutSets(**workout_set_data.model_dump(), workout_id=workout_id)
    db.add(new_workout_set)
    await db.commit()
    await db.refresh(new_workout_set)
    return new_workout_set