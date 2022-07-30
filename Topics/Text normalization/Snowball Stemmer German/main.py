from nltk.stem import SnowballStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()

snowball = SnowballStemmer('german')
for n in sent:
    print(snowball.stem(n))