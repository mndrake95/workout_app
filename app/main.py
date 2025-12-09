from fastapi import FastAPI

app = FastAPI(title="Workout Tracker")

@app.get("/")
def read_root():
    return {"message": "System Online"}