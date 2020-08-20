from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

en_stopwords = set(stopwords.words('english'))
tokenizer = nltk.RegexpTokenizer(r'\w+')


class NltkTokenizer:
    def tokenize(self, document):
        return word_tokenize(document)


def tokenize_document(document, tokenizer=NltkTokenizer(), remove_stopwords=True):
    tokens = tokenizer.tokenize(document)
    return [token for token in tokens if not remove_stopwords or token not in en_stopwords]


def tokenize_document_pretty(document, tokenizer=word_tokenize):
    result = []
    for line in document.split('\n'):
        result.append(' '.join(tokenize_document(line, tokenizer)))
    return '\n'.join(result)
