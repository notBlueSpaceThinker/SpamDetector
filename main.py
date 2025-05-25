from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
import uuid
import shutil

from core.file_loader import read_text_file
from core.text_cleaner import clean_text
from core.spam_filter import is_spam

BASE_DIR = os.path.dirname(__file__)
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

#модель для return
class ReturnData(BaseModel):
    filename: str
    is_spam: bool
    cleaned_text: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#подкрутить очистку uploads через shutil ?
@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...)):
    #cоздание уникального имени файла и сохранение пути в filepath
    filename = f"{uuid.uuid5()}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)  

    #сохранение файла в uploads
    with open(filepath, "wb") as buffer:                
        shutil.copyfileobj(file.file, buffer)           


    # ReturnData.filename = filename
    # ReturnData.cleaned_text = clean_text(cleaned)
    # ReturnData.is_spam = is_spam(ReturnData.cleaned_text)

    raw = read_text_file(filepath)
    cleaned = clean_text(raw)
    result = is_spam(cleaned)

    return {
        "filename": file.filename,
        "is_spam": result,
        "cleaned_text": cleaned
    }

