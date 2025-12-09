from pydantic import BaseModel, ConfigDict
import uuid
import datetime

class ExerciseBase(BaseModel):
    title: str
    type: str
    body_parts: list[str]

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseRead(ExerciseBase):
    id: uuid.UUID
    created_at: datetime.datetime
    model_config = ConfigDict(from_attributes=True)

class WorkoutBase(BaseModel):
    name: str|None = None

class WorkoutCreate(WorkoutBase):
    pass

class WorkoutRead(WorkoutBase):
    id: uuid.UUID
    owner_id: int
    created_at: datetime.datetime
    model_config = ConfigDict(from_attributes=True)

class WorkoutSetBase(BaseModel):
    reps: int|None = None
    weight: float|None = None
    set_order: int
    distance: float|None = None
    duration: int|None = None

class WorkoutSetCreate(WorkoutSetBase):
    exercise_id: uuid.UUID

class WorkoutSetRead(WorkoutSetBase):
    id: uuid.UUID
    workout_id: uuid.UUID
    exercise_id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)
