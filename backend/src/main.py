from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import task_route

# Everything in here is to basically totally initalize everything, I made everything separate so there would be easier debugging

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:5173",
]

# This line is important and above if you want to allow your frontend to get the reequests and for backend to process it
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_route.router)

@app.get("/")
def get_root():
    return {
        "message" : "Hello, World"
    }