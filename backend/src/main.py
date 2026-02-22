from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=200)
def main():
    return {
        "ok": True
    }