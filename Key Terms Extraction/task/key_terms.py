import string
import nltk
from lxml import etree

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


def tokenize(text):
    text = text.replace("co-lead", "lead")
    tokenized = nltk.word_tokenize(text)
    lemmatized = [WordNetLemmatizer().lemmatize(word, pos='n') for word in tokenized]
    nn_list = [word for word in lemmatized if nltk.pos_tag([word])[0][1] == 'NN']
    return nn_list


xml_file = "news.xml"
root = etree.parse(xml_file).getroot()
dataset = []
titles = []
stopwords = list(stopwords.words('english')) + list(string.punctuation) + ['ha', 'wa', 'u', 'a', 'doe', 'need', 'sha']
for news in root[0]:
    titles.append(news[0].text)
    dataset.append(news[1].text.lower())
vectorizer = TfidfVectorizer(lowercase=True, tokenizer=tokenize, stop_words=stopwords)
tfidf_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names_out()
dimension = tfidf_matrix.shape
row = 0
while row < dimension[0]:
    print(titles[row], end=":\n")
    column = 0
    word_rate = []
    while column < dimension[1]:
        if tfidf_matrix.toarray()[row][column] != 0:
            word_rate.append((terms[column], tfidf_matrix.toarray()[row][column]))  # first value = word , second value = rate
        column += 1
    sorted_words = sorted(word_rate, key=lambda x: (x[1], x[0]), reverse=True)[0:5]
    print(*[i[0] for i in sorted_words])
    row += 1


