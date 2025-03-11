from fastapi import FastAPI, File, UploadFile, Form
from typing import List

app = FastAPI()

@app.post("/upload-single/")
def upload_single(file: UploadFile = File(...)):
    return {"filename": file.filename, "content_type": file.content_type}

@app.post("/upload-multiple/")
def upload_multiple(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

@app.post("/submit-form/")
def submit_form(name: str = Form(...), email: str = Form(...)):
    return {"name": name, "email": email}

# Run with: uvicorn file_upload:app --reload
