import os 
import pandas

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "spam_dataset.xlsx")

spam_data = pandas.read_excel(file_path, engine='openpyxl', header=None)

temp_spam_dict = {}
for _, row in spam_data.iterrows():
    if len(row) >= 2:
        spam_word = str(row[0]).strip()
        try:
            value = int(row[1])
            temp_spam_dict[spam_word] = value
        except ValueError:
            raise ValueError(f"Ошибка в строке: {row.values}")

SPAM_KEYWORDS = temp_spam_dict
SPAM_URLS = {"https://www.hse.ru": 3} #in progress

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