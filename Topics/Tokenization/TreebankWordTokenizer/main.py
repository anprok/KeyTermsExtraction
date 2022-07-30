from nltk.tokenize import TreebankWordTokenizer

text = input()
tbw = TreebankWordTokenizer()
print(tbw.tokenize(text))