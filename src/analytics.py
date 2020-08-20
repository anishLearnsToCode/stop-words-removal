import pickle
from utils import tokenize_document, tokenizer
from collections import Counter

tokens_with_stopwords = tokenize_document(open('../assets/resume.txt', 'r').read(), tokenizer, remove_stopwords=False)
print('Number of Tokens: (with stopwords)', len(tokens_with_stopwords))
print('Number of Unique tokens: (with stopwords)', len(set(tokens_with_stopwords)), '\n')

tokens = pickle.load(open('../assets/resume_tokens.p', 'rb'))
print('Number of Tokens: (without stopwords)', len(tokens))
tokens_set = set(tokens)
print('Number of Unique tokens: (without stopwords)', len(tokens_set))

print('\nPercentage Reduction in tokens after removing stopwords:',
      (len(set(tokens_with_stopwords)) - len(tokens_set)) / len(tokens_set) * 100
)

frequencies = Counter(tokens)
print('\nThe Frequencies of the most common 10 tokens are: (in tokens without stopwords)\n', frequencies.most_common(10))
