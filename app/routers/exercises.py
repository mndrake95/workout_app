from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas import ExerciseCreate, ExerciseRead
from app.models import Exercise
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=ExerciseRead)
async def create_exercise(
    exercise_data: ExerciseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_exercise = Exercise(**exercise_data.model_dump())
    db.add(new_exercise)
    await db.commit()
    await db.refresh(new_exercise)
    return new_exercise

@router.get("/", response_model=list[ExerciseRead])
async def read_exercise(
    db: AsyncSession = Depends(get_db)
):
    query = select(Exercise)
    result = await db.execute(query)
    return result.scalars().all()