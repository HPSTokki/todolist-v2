from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exception import DomainException

app = FastAPI()

@app.exception_handler(DomainException)
async def handle_exception(req: Request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.message
        }
    )

@app.get("/", status_code=200)
def main():
    return {
        "ok": True
    }