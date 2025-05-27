import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def extract_links(text: str) -> list[str]:
    links = re.findall(r'(https?://\S+|www\.\S+)', text)
    if not links:
        print("Файл без ссылок")
        
    return links

def extract_tokens(text: str) -> list[str]:
    if not text:
        print("Файл без текста")
        return ""
    if not text.isascii():
        raise ValueError("Поддерживаются только файлы на Английском языке")

    text = re.sub(r"<.*?>", "", text)

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        lemmatizer.lemmatize(t)
        for t in tokens
        if t.isalpha() and t not in stop_words
    ]

    print(f"Токены: {tokens}")

    return tokens

def extract_tokens_and_links(text: str) -> tuple[str, list[str]]:
    if not text:
        print("Файл без текста")
        return "", []
    
    links = extract_links(text)
    tokens = extract_tokens(text)

    return tokens, links 