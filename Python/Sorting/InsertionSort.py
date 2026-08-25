def InsertionSort(l):
    for i in range(1,len(l)):
        temp = l[i]
        j = i - 1

        while j>= 0 and l[j] > temp:
            l[j+1] = l[j]
            j-= 1

        l[j+1] = temp

    return l

list1 = [9,2,4,7,3,8,5]
print(InsertionSort(list1))