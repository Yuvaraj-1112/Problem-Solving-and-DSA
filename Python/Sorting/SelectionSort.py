def SelectionSort(l):
    for i in range(len(l)):
        min_val = i

        for j in range(i+1, len(l)):
            if l[j] < l[min_val]:
                min_val = j

        (l[i], l[min_val]) = (l[min_val], l[i])

    return l

list1 = [9,2,4,7,3,8,5]
print(SelectionSort(list1))