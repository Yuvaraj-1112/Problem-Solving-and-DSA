arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

first_neg = 0

for i in range(len(arr) - k + 1):

    while ( first_neg < i + k and
        (first_neg < i or arr[first_neg] >= 0) ):
        
        first_neg += 1

    if first_neg < i + k:
        print(arr[first_neg], end=" ")
    else:
        print(0, end=" ")