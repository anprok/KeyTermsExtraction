from collections import Counter
text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        + "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

n = int(input())
freq_counter = Counter(text.split())

for key, val in freq_counter.most_common(n):
    print(key, val)