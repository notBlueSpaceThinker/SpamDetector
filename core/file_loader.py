def read_text_file(path: str) -> str:
    try:
        with open(path, 'r', encoding = 'utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("Файл не найден")
        return ""
    except Exception as e:
        print(f"Ошибка {e} при чтении файла")
        return ""
