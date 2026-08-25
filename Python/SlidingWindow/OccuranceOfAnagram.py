'''
s = "forxxorfxdofr"
p = "for"

Answer = 3

Answer = 3
Explanation : for, orf, ofr = 3

'''

from collections import Counter

def occur_of_anagram(s, p):
    k = len(p)

    p_freq = Counter(p)
    w_freq = Counter(s[:k])

    count = 0

    if p_freq == w_freq:
        count += 1

    for i in range(k, len(s)):
        w_freq[s[i]] += 1

        w_freq[s[i-k]] -= 1

        if w_freq[s[i-k]] == 0:
            del w_freq[s[i-k]]

        if w_freq == p_freq:
            count += 1

    return count

s = "forxxorfxdofr"
p = "for"

print(occur_of_anagram(s, p))