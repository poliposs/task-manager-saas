from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, welcome to Task Manager API!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}