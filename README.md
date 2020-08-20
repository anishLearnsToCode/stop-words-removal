# Stopwords Removal From a Corpus
__Anish Sachdeva (DTU/2K16/MC/013)__

__Natural Language Processing - Dr. Seba Susan__

[[Running Notebook 📔]](https://github.com/anishLearnsToCode/stop-words-removal/blob/master/notebook/removing-stop-words.ipynb) 
[[Input 📄]](https://github.com/anishLearnsToCode/stop-words-removal/blob/master/assets/resume.txt) 
[[Code to print Output 📄]](https://github.com/anishLearnsToCode/stop-words-removal/blob/master/src/output.py)
[[Project Report 🌟]]()

![stopwords-english](assets/stopwords-en.png)

## Overview
1. [Introduction](#introduction)
1. [Implementation](#implementation)
1. [Results](#results)
1. [Analytics & Discussions](#analytics--discussion)
1. [Running The Project Locally](#running-project-locally)
1. [Bibliography](#bibliography)

## Introduction
Normally the following steps are very commonly and ubiquitously implemented as part of the data
preprocessing pipeline in any NLP project:
1. Converting the entire corpus into a common case (either lowercase or uppercase)
1. Extracting words/tokens from the corpus
1. Removing all Punctuations from the selected tokens and retaining only alphanumeric quantities
1. Removing all Stopwords from the extracted tokens. 
1. Stemming the Token into it's root with any Stemming Algorithm

We have seen Stemming in detail in the 
[Porter Stemmer Assignment](https://github.com/anishLearnsToCode/porter-stemmer)
& in this notebook we see how to extract tokens, remove punctuation and remove stopwords. 

## Implementation
The implementation uses the popular 
[nltk](https://www.nltk.org/)
(Natural Language Processing Toolkit) for removing stopwords, tokenization and stemming.
The entire process has been sown in detail in
[this Jupyter Notebook](https://github.com/anishLearnsToCode/stop-words-removal).

## Results
The input for this program was my Resume in text format that can be viewed
[here: resume.txt](assets/resume.txt). 
The output is a stream of tokens (words) that has been converted to lowercase and also
the punctuations and stopwords have been removed. The output has been saved as pickle
file and can be loaded into any Python file (or Jupyter Notebook) and can be viewed
in the Notebook [here](https://render.githubusercontent.com/view/ipynb?commit=9cb010f6c04b8770224d131a5a21ccee6cc07a6c&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f616e6973684c6561726e73546f436f64652f73746f702d776f7264732d72656d6f76616c2f396362303130663663303462383737303232346431333161356132316363656536636330376136632f6e6f7465626f6f6b2f72656d6f76696e672d73746f702d776f7264732e6970796e62&nwo=anishLearnsToCode%2Fstop-words-removal&path=notebook%2Fremoving-stop-words.ipynb&repository_id=288802890&repository_type=Repository#7.-Creating-Formatted-(Pretty)-Output)
or in [the Pickle File](assets/resume_tokenized.p).

## Analytics & Discussion
We have seen that after removing the stopwords from the resume our number of words has gone down considerably and also
that the words we removed never added a lot of meaning to our text. Large companies who will receive many resumes 
will want to search them using keywords such as Java, Python, web Development etc. and words such as 
i, me, mine are superfluous in nature.

So, by removing these stopwords we have actually made our corpus more information dense and any other further task we 
might perform such as converting these words into embeddings or any other Machine Learning/Deep Learning task will now 
be done on a smaller Corpus and hence would run faster.

Considering these above advantages removing stopwords is a very beneficial pre-processing step.

## Running Project Locally
To run this project locally and see the output of the resume file once the stop words have been removed, first clone 
the project and enter the project directory.
```bash
git clone https://github.com/anishLearnsToCode/stop-words-removal.git
cd stop-words-removal
``` 

Install required packages
```bash
pip install nltk
pip install pickle
```
Run the `driver.py` file to see stream of tokens as output and then run the `analytis.py`
file to see various analytics on the prepared token list.
```bash
python driver.py
python analytics.py
```

Run the `output.py` file to see a pretty (well formatted) output of the resume. 
```bash
python output.py
```

## Bibliography
1. [Speech & Language Processing ~Jurafsky](https://web.stanford.edu/~jurafsky/slp3/)
1. [nltk](https://www.nltk.org/)
1. [pickle](https://docs.python.org/3/library/pickle.html)
1. [Porter Stemmer Algorithm](http://tartarus.org/martin/PorterStemmer)
1. [Porter Stemmer Implementation ~anishLearnsToCode](https://github.com/anishLearnsToCode/porter-stemmer)
1. [English Stopwords ~Wikipedia](https://en.wikipedia.org/wiki/Stop_words)
