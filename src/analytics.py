import pickle
from collections import Counter

tokens = pickle.load(open('../assets/resume_tokens.p', 'rb'))
print('Number of Tokens:', len(tokens))
tokens_set = set(tokens)
print('Number of Unique tokens:', len(tokens_set))

frequencies = Counter(tokens)
print('\n\nThe Frequencies of the most common 10 tokens are:\n', frequencies.most_common(10))
