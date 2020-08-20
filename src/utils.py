from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
en_stopwords = set(stopwords.words('english'))


def tokenize_document(document, tokenizer=word_tokenize):
    tokens = tokenizer.tokenize(document)
    return [token for token in tokens if token not in en_stopwords]


def tokenize_document_pretty(document, tokenizer=word_tokenize):
    result = []
    for line in document.split('\n'):
        result.append(' '.join(tokenize_document(line, tokenizer)))
    return '\n'.join(result)
