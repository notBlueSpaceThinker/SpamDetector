def read_text_file(path: str) -> str:
    with open(path, 'r', encoding = 'utf-8') as f:
        return f.read()

# def read_text_file(path: str) ->str:
#     try:
#         with open(path, 'r', encoding = 'utf-8') as f:
#             return f.read()
#     except FileNotFoundError:
#         print("Файл не был найден в директории")
#         return ""