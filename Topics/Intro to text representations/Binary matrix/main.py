from nltk import word_tokenize, sent_tokenize

import numpy as np


def tokenize(sentences):
    # tokenize all 3 sentences; do not lemmatize/stem them
    # make a list of tokens
    # append this list to a bigger list of all 3 sentences
    tokenized = []
    for text in sentences:
        tokenized.append(word_tokenize(text.lower()))
    return tokenized


def make_vocabulary(tokens_list):
    # make your own vocabulary here
    # tokens in your vocabulary should have only lowercase
    vocabulary_list = []
    for token_text in tokens_list:
        for token in token_text:
            vocabulary_list.append(token)
    return sorted(set(vocabulary_list))


def make_matrix(vocabulary_list, texts_list):
    matrix = np.zeros((len(texts_list), len(vocabulary_list)))
    # make a binary matrix
    for n, _ in enumerate(texts_list):
        for m, _ in enumerate(vocabulary_list):
            if vocabulary_list[m] in texts_list[n]:
                matrix[n][m] = 1
    return matrix


corpus = str(input())  # you get a string of 3 sentences
texts = list(sent_tokenize(corpus))  # list of 3 strings-sentences
tokens = tokenize(texts)  # word_tokenize your sentences
vocabulary = make_vocabulary(tokens)  # use these tokens to make a vocabulary
print(make_matrix(vocabulary, tokens))  # make a matrix
