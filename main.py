from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
import uuid
import shutil

from core.file_loader import read_text_file
from core.text_cleaner import extract_tokens, extract_links
from core.spam_filter import is_spam

# Определения директории проекта и пути к папке для загрузки файлов
BASE_DIR = os.path.dirname(__file__)
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

# Создание uploads
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

# Подключение папки со статикой
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Вывод пользователу HTML шаблона 
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Обработка загруженного файла
@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.txt'):
        raise HTTPException(status_code=400, detail = "Поддерживаются только текстовые файлы")
    
    # Создание уникального имени файла и сохранение пути в filepath
    filename = f"{uuid.uuid4()}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)  

    #Сохранение файла в uploads
    with open(filepath, "wb") as buffer:                
        shutil.copyfileobj(file.file, buffer)           

    # Проверочные принты
    # print("Raw:", raw)
    # print("Cleaned:", cleaned)
    # print("Links:", extract_links(raw))

    # Основная логика и вызов функций обработки текста
    try:
        raw = read_text_file(filepath)
        cleaned = extract_tokens(raw)
        result = is_spam(cleaned)
    except Exception as e:
        raise HTTPException(status_code=400, detail = f"Ошибка в обработке файла: {str(e)}")

    # Очистка файла из uploads
    os.remove(filepath)
    
    return {
        "filename": file.filename,
        "is_spam": result,
        "cleaned_text": cleaned
    }