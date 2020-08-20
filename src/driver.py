import nltk
from utils import tokenize_document_pretty

resume_file = open('../assets/resume.txt', 'r')
resume = resume_file.read()
resume_file.close()

tokenizer = nltk.RegexpTokenizer(r'\w+')
resume_tokenized = tokenize_document_pretty(resume, tokenizer)
print(resume_tokenized)
