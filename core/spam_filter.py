import csv
import os 

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "spam_dataset.csv")

temp_spam_dict = {}
with open(file_path, newline='', encoding='utf-8') as csvdataset:
    reader = csv.reader(csvdataset, delimiter='\t')
    for row in reader:
        if len(row) == 2:
            word = row[0].strip()
            try:
                value = int(row[1].strip())
                temp_spam_dict[word] = value
            except ValueError:
                print("Ошибка в data-сете")
                raise ValueError(f"Не удается преобразовать строчку {row}")

SPAM_KEYWORDS = temp_spam_dict
SPAM_URLS = {"https://www.hse.ru": 3} #in process


def is_spam(text: str|list[str], threshold: float = 0.3) -> bool:
    if isinstance(text, list):
        text = " ".join(text)

    text_lower = text.lower()
    total_words = len(text_lower.split())
    if total_words == 0:
        return False
    
    spam_values_count = 0
    for keyword, value in {**SPAM_KEYWORDS, **SPAM_URLS}.items():
        if keyword in text_lower:
            spam_values_count += value


    spam_ratio = spam_values_count / total_words
    return spam_ratio >= threshold