def count_freq(s1):
    freq = {}
    for char in s1:
        if char != ' ':
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

    return freq


s1 = 'My name is Rahul'
result = count_freq(s1)
print(result)
