from fastapi import FastAPI

# create fastapi instance
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "good job..."
    }

@app.get("/new")
def new():
    return {
        "message": "new..."
    }