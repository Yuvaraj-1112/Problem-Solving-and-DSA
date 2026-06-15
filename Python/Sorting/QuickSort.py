def QuickSort(l,left,right):

    if right - left <= 1:
        return()
    
    small = left + 1

    for big in range(left +1,right):
        if l[big] <= l[left]:
            (l[small], l[big]) = (l[big], l[small])
            small += 1

    (l[left], l[small - 1]) = (l[small - 1], l[left])

    QuickSort(l,left, small -1)
    QuickSort(l,small, right)

    return l

a = [9,8,7,6,5,4,0,3,2,1]
print(QuickSort(a,0,len(a)))