SPAM_KEYWORDS = ["win", "free", "money", "click", "offer", "urgent", "buy now", "lottery"]

def is_spam(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in SPAM_KEYWORDS)
