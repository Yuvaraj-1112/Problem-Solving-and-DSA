def SelectionSort(l):
    for start in range(len(l)):

        minpos = start
    
        for i in range(start,len(l)):
            if l[i] < l[minpos]:
                minpos = i
        
        (l[start], l[minpos]) = (l[minpos], l[start])

    return l

list1 = [9,2,4,7,3,8,5]
print(SelectionSort(list1))