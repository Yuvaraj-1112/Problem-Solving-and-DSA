n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
freq = {}
max_len = 0

for right in range(n):
    # Add current pizza flavor
    freq[arr[right]] = freq.get(arr[right], 0) + 1

    # Shrink window if distinct flavors exceed k-1
    while len(freq) > k - 1:
        freq[arr[left]] -= 1

        if freq[arr[left]] == 0:
            del freq[arr[left]]

        left += 1

    # Update maximum valid window length
    max_len = max(max_len, right - left + 1)

print(max_len)
