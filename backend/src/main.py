from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.exception import DomainException

app = FastAPI()

@app.exception_handler(DomainException)
async def domain_exception(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.message
        }
    )

@app.get("/")
async def main():
    return {
        "ok": True
    }