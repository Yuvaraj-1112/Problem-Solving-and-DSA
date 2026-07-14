def BubbleSort(l1):
    swap = False

    n = len(l1)

    for i in range(n):
        for j in range(n-i-1):
            if l1[j] > l1[j+1]:
                (l1[j], l1[j+1]) = (l1[j+1], l1[j]) 
                swap = True

        if swap is False:
            break

    print(l1)

l1 = [0,3,5,6,7,2]
BubbleSort(l1)