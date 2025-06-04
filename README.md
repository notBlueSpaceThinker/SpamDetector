Spam Detector

Проект для анализа текстовых файлов на предмет спама.  
Используется FastAPI для веб-интерфейса, NLTK для обработки текста и простой словарный фильтр в виде .xlsx таблицы для определения спама.

### Особенности

- Загрузка файлов через веб-интерфейс (drag-n-drop или выбор файла)
- Анализ текста на спам с выводом результата и очищенного текста
- Маштабируемость проекта
- Легко расширяемая логика фильтрации

### Структура проекта

<details>
<summary>Нажми, чтобы раскрыть</summary>

```plaintext
spam_detector/
├── core/
│   ├── file_loader.py       # Загрузка и чтение текстов
│   ├── text_cleaner.py      # Очистка текста
│   └── spam_filter.py       # Фильтрация спама
│
├── data/                   # Вспомогательные данные (словари, примеры и т.п.)
│   └── sample_messages.txt
│
├── uploads/                # Загруженные пользователем файлы
│
├── static/
│   ├── style.css           # Стили интерфейса
│   └── script.js           # Скрипт для загрузки файлов
│
├── templates/
│   └── index.html          # Jinja2-шаблон главной страницы
│
├── main.py                 # Основной файл FastAPI-приложения
└── requirements.txt        # Зависимости проекта
```
</details> 

### 💫 Как запустить проект

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/notBlueSpaceThinker/SpamDetector
    cd spam_detector
    ```

2. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv venv
    venv\Scripts\activate     # для Windows
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Запустите приложение:**

    ```bash
    uvicorn main:app --reload
    ```

5. **Откройте в браузере:**

    ```
    http://127.0.0.1:8000
    ```
