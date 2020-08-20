import nltk
import pickle
from utils import tokenize_document

resume_file = open('../assets/resume.txt', 'r')
resume = resume_file.read()
resume_file.close()

tokenizer = nltk.RegexpTokenizer(r'\w+')
resume_tokenized = tokenize_document(resume, tokenizer)
print(resume_tokenized)
pickle.dump(resume_tokenized, open('../assets/resume_tokens.p', 'wb'))
