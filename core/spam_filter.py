SPAM_KEYWORDS = ["win"]
SPAM_URLS = ["https://www.hse.ru"]

#НАДО ДОДЕЛАТЬ ЭТУ ЛОГИКУ АЛЕ
def is_spam(text: str|list[str], threshold: float = 0.3) -> bool:
    if isinstance(text, list):
        text = " ".join(text)

    text_lower = text.lower()
    total_words = len(text_lower.split())
    if total_words == 0:
        return False
    
    spam_word_count = 0
    for keyword in SPAM_KEYWORDS + SPAM_URLS:
        if keyword in text_lower:
            spam_word_count += 1

    spam_ratio = spam_word_count / total_words
    return spam_ratio >= threshold
