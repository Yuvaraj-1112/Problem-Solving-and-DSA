def InsertionSort(l):
    for silceEnd in range(len(l)):

        pos = silceEnd

        while pos > 0 and l[pos] < l[pos - 1]:
            (l[pos], l[pos - 1]) = (l[pos - 1], l[pos])
            pos = pos - 1
    
    return l

list1 = [9,2,4,7,3,8,5]
print(InsertionSort(list1))