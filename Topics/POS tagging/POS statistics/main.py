from collections import Counter

import nltk

pos_list = [pos for (_, pos) in nltk.pos_tag(input().split())]
print(Counter(pos_list).most_common(1)[0][0])
