import string


def clean_phrase(phrase: str) -> str:
    words = map(lambda x: x.strip(string.punctuation), phrase.lower().split())
    return ' '.join(words)