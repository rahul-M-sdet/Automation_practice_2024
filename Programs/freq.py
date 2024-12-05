from collections import Counter


def count_freq(s1):
    return Counter(s1)


s1 = 'programming'
count = count_freq(s1)
print(count)
