import nltk

tokens = nltk.tokenize.word_tokenize(input())
pos_list = {}
for _, pos in nltk.pos_tag(tokens):
    pos_list.setdefault(pos, 0)
    pos_list[pos] += 1
print(pos_list)
