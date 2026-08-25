'''arr = [12,-1,-7,8,-15,30,16,28]
k = 3

Output:
-1 -1 -7 -15 -15 0

explanation: 12 -1 -7 = -1 ... upto last'''

def first_neg_subarray(arr, k):
    for i in range(len(arr) - k + 1):
        found = False

        for j in range(i, i+k):

            if arr[j] < 0:
                print(arr[j], end=" ")
                found = True
                break

        if not found:
            print(0, end=" ")



arr = [12,-1,-7,8,-15,30,16,28]
k = 3

first_neg_subarray(arr,k)
