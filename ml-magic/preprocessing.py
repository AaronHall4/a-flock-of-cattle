
import nltk
from nltk.corpus import stopwords
import numpy as np
import string


def get_word_toks(data):
    tokens = nltk.word_tokenize(data.lower())
    
    stops = set(stopwords.words('english'))
    wo_stops = [t for t in tokens if t not in stops]

    stemmer = nltk.stem.PorterStemmer()
    stemmed = [stemmer.stem(w) for w in  wo_stops]
    
    punc_table = {}
    for c in string.punctuation:
        punc_table[ord(c)] = None
    wo_punc = [w.translate(punc_table) for w in stemmed]
    empty_filtered = [w for w in wo_punc if w != '']

    return wo_punc
