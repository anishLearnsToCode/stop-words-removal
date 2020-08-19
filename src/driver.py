import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

en_stopwords = set(stopwords.words('english'))

resume_file = open('../assets/resume.txt', 'r')
resume = resume_file.read()
resume_file.close()

tokenizer = nltk.RegexpTokenizer(r'\w+')

tokens = tokenizer.tokenize(resume)
updated_tokens = [token for token in tokens if token not in en_stopwords]
print(tokens[:40])
print(updated_tokens[:40])

stemmer = PorterStemmer()
print(stemmer.stem('running'))

stemmed_tokens = [stemmer.stem(token) for token in updated_tokens]
print(stemmed_tokens)
