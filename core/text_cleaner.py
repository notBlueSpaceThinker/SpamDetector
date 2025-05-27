import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# word definition
# from nltk.corpus import wordnet as wn -> wn.synsets()


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def extract_links(text: str) -> list[str]:
    links = re.findall(r'(https?://\S+|www\.\S+)', text)
    return links

# lemmatizer.morphy
# Попробовать вариант в очисткой токенизированных слов и отправкой
# токенезированного списка предложений
def clean_text(text: str) -> str:
    if not text:
        print("Файл без текста")
        return ""

    text = re.sub(r"<.*?>", "", text)

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        lemmatizer.lemmatize(t)
        for t in tokens
          if t.isalpha() and t not in stop_words
    ]

    print(f"{tokens}")

    return " ".join(tokens)