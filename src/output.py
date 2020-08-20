import nltk
from utils import tokenize_document_pretty

tokenizer = nltk.RegexpTokenizer(r'\w+')
resume_file = open('../assets/resume.txt', 'r')
resume = resume_file.read()
resume_file.close()

print(tokenize_document_pretty(resume, tokenizer))
