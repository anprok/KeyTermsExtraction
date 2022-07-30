from nltk.stem import WordNetLemmatizer
word = input()
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(word, pos='n'))
print(lemmatizer.lemmatize(word, pos='a'))
print(lemmatizer.lemmatize(word, pos='v'))