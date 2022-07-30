from nltk import regexp_tokenize, sent_tokenize

sentences = sent_tokenize(input())
print(regexp_tokenize(sentences[int(input())], "[A-z']+"))