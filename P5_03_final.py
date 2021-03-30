# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:21:42 2021

@author: AzertWay
"""
from bs4 import BeautifulSoup
import re
import unicodedata
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from joblib import load

stopwords = set(nltk.corpus.stopwords.words('english'))


def remove_accents(text):
    '''Given text, removes the accents

    Parameters
    ----------
    text: str

    Returns
    -------
    str (text without accents)

    '''

    return unicodedata.normalize('NFKD', text)\
            .encode('ascii', errors='ignore').decode('utf-8')


def comments_to_words(comment):
    ''' Puts the comment in lower case, removes accents, tokenizes the text
    and returns the tokens

    Parameters
    ----------
    comment: str

    Returns
    -------
    tuple (tokens)

    '''

    lowered = comment.lower()
    normalized = remove_accents(lowered)
    tokens = nltk.tokenize.word_tokenize(normalized)

    mwetokenizer = nltk.tokenize.mwe.MWETokenizer(separator='')
    mwe_list = [('c', '#'), ('C', '#'), ('f', '#'), ('F', '#')]
    for mwe in mwe_list:
        mwetokenizer.add_mwe(mwe)
    tokens = mwetokenizer.tokenize(tokens)

    words = tuple(t for t in tokens if t not in stopwords and
                  ((t.isalnum() and not t.isdigit()) or ('#' in t)))
    return words


def raw_text_to_words(raw_comment):
    ''' Convert a raw comment into a string of words

    Parameters
    ----------
    raw_comment: str

    Returns
    -------
    str (assembled lemmatized tokens)

    '''

    # 1. Remove HTML
    comment_text = BeautifulSoup(raw_comment, 'html.parser')

    # 2. Remove non-letters non-digits
    letters_only = re.sub("[^a-zA-Z0-9#+.-]", " ", comment_text.get_text())

    # 3. Convert to lower case, remove accents, tokenize
    # and remove stop words
    meaningful_words = comments_to_words(letters_only)

    # 4. Lemmatization
    lemmatizer = WordNetLemmatizer()
    meaningful_words_lemmatized = tuple(lemmatizer.lemmatize(t)
                                        for t in meaningful_words)

    # 5. Join the words back into one string separated by space
    return " ".join(meaningful_words_lemmatized)


def remove_nan(y):
    for i in range(len(y)):
        y[i] = list(y[i])
        if 'nan' in y[i]:
            y[i].remove('nan')


def classification(args):
    ''' Given a corpus returns the tags associated with each comment
    '''
    
    comment = args['Title'] + '\n\n' + args['Body']
    
    lemmitized_words = raw_text_to_words(comment)
    
    clf = load('final_model.joblib')
    encoder = load('encoder.joblib')
    
    tags_b = clf.predict([lemmitized_words])
    tags = encoder.inverse_transform(tags_b)
    remove_nan(tags)
    
    return tags, 200
