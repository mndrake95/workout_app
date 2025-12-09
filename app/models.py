import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy import func
import datetime
from .database import Base

class Exercise(Base):
    __tablename__ = "exercises"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    body_parts: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())

class Workout(Base):
    __tablename__ = "workouts"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str|None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    sets = relationship("WorkoutSets", back_populates="workout", cascade="all, delete-orphan")

class WorkoutSets(Base):
    __tablename__ = "workout_sets"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("workouts.id"), nullable=False)
    exercise_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercises.id"), nullable=False)    
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    set_order: Mapped[int] = mapped_column(Integer, nullable=False)
    distance: Mapped[float|None] = mapped_column(Float, nullable=True)
    duration: Mapped[float|None] = mapped_column(Float, nullable=True)
    workout = relationship("Workout", back_populates="sets")