# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:21:42 2021

@author: AzertWay
"""
import pandas as pd
from bs4 import BeautifulSoup
import re
import unicodedata
import nltk
from nltk.stem import WordNetLemmatizer

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
                  ((t.isalnum() and not t.isdigit()) or ('#' in t)) and
                  (len(t) > 1))
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
    letters_only = re.sub("[^a-zA-Z0-9#+.]", " ", comment_text.get_text())

    # 3. Convert to lower case, remove accents, tokenize
    # and remove stop words
    meaningful_words = comments_to_words(letters_only)

    # 4. Lemmatization
    lemmatizer = WordNetLemmatizer()
    meaningful_words_lemmatized = tuple(lemmatizer.lemmatize(t)
                                        for t in meaningful_words)

    # 5. Join the words back into one string separated by space
    return(" ".join(meaningful_words_lemmatized))


def classification(*args):
    ''' Given a corpus returns the tags associated with each comment
    '''

    raw_data = pd.read_csv(*args)
    
    raw_data['Comment'] = raw_data.Title + '\n\n' + raw_data.Body
    
    raw_data = raw_data.sample(frac=.2, random_state=47)
    #n_features = len(raw_data)
    
    raw_data['Words'] = raw_data['Comment']\
        .apply(lambda raw_text: raw_text_to_words(raw_text))
        
    
    return raw_data.iloc[:10, -1].to_dict()

def append_data(args):
    ''' adds a new comment in the corpus
    '''

    raw_data = pd.read_csv(args['file_path'])
    
    if int(args['Id']) in list(raw_data['Id']):
        return f"'{args['Id']}' already exists.", 409

    else:
        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'Id': [args['Id']],
            'Title': [args['Title']],
            'Body': [args['Body']]
        })
        
        # add the newly provided values
        raw_data = raw_data.append(new_data, ignore_index=True)
        raw_data.to_csv(args['file_path'], index=False)
        return raw_data.iloc[-1, -1], 201

def delete_data(args):
    ''' drops a comment from the corpus
    '''

    raw_data = pd.read_csv(args['file_path'])
    
    if int(args['Id']) in list(raw_data['Id']):
        # remove data entry matching given userId
        raw_data = raw_data[raw_data['Id'] != int(args['Id'])]
            
        # save back to CSV
        raw_data.to_csv(args['file_path'], index=False)
        # return data and 200 OK
        return None, 204
    else:
        # otherwise we return 404 because Id does not exist
        return f"'{args['Id']}' user not found.", 404
