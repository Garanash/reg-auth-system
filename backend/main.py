import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "main page"

if __name__ == "__main__":
    uvicorn.run(app, port=8001)

