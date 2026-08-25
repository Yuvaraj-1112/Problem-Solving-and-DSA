'''
a = [3,1,4,3,2,2,4]
k = 2

answer = 4
Explanation: [3,1,4,3,2,2] [1,4,3,2,2,4] [4,3,2,2,4] [3,1,4,3,2,2,4]
'''

from collections import defaultdict
a = [3,1,4,3,2,2,4]
k = 2

n = len(a)
freq = defaultdict(int)
l = 0
pairs = 0
legpairs = 0

for r in range(n):
    pairs += freq[a[r]]
    freq[a[r]] += 1

    while pairs >= k:
        legpairs += n - r
        freq[a[l]] -= 1
        pairs -= freq[a[l]]
        l += 1

print(legpairs)

