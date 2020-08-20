# Stopwords Removal From a Corpus
__Anish Sachdeva (DTU/2K16/MC/013)__

__Natural Language Processing - Dr. Seba Susan__

## Overview
1. [Introduction](#introduction)
1. [Implementation](#implementation)
1. [Results](#results)
1. [Analytics & Discussions](#analytics--discussion)
1. [Bibliography](#bibliography)

## Introduction
Normally the following steps are very commonly and ubiquitously implemented as part of the data
preprocessing pipeline in any NLP project:
1. Converting the entire corpus into a common case (either lowercase or uppercase)
1. Extracting words/tokens from the corpus
1. Removing all Punctuations from the selected tokens and retaining nly alphanumeric quantities
1. Removing all Stopwords from the extracted tokens. 
1. Stemming the Token into it's root with any Stemming Algorithm

We have seen Stemming in detail in the 
[Porter Stemmer Assignment](https://github.com/anishLearnsToCode/porter-stemmer)
& in this notebook we see how to extract tokens, remove punctuation and removing stopwords. 

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
in the Notebook [here]()
or in [the Pickle File]().

## Analytics & Discussion


## Bibliography
1. [Speech & Language Processing ~Jurafsky](https://web.stanford.edu/~jurafsky/slp3/)
1. [nltk](https://www.nltk.org/)
1. [pickle](https://docs.python.org/3/library/pickle.html)
1. [Porter Stemmer Algorithm](http://tartarus.org/martin/PorterStemmer)
1. [Porter Stemmer Implementation ~anishLearnsToCode](https://github.com/anishLearnsToCode/porter-stemmer)
1. [English Stopwords ~Wikipedia](https://en.wikipedia.org/wiki/Stop_words)
