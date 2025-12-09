from fastapi import FastAPI
from app.routers.exercises import router as exercises_router
from app.routers.workouts import router as workouts_router
from app.routers.workout_sets import router as workout_sets_router

app = FastAPI(title="Workout Tracker")

@app.get("/")
def read_root():
    return {"message": "System Online"}

app.include_router(exercises_router, prefix="/exercises", tags=["Exercises"])
app.include_router(workouts_router, prefix="/workouts", tags=["Workouts"])
app.include_router(workout_sets_router, prefix="/workouts", tags=["WorkoutSets"])