def QuickSort(arr,srt,end):

    if srt < end:

        pivot = Partition(arr,srt,end)
        QuickSort(arr,srt,pivot-1)
        QuickSort(arr,pivot+1,end)

def Partition(a,srt,end):

    piv_val = a[srt]

    i = srt + 1
    j = end

    while i < j:
        while i < end and a[i] <= piv_val:
            i += 1

        while j > srt and a[j] > piv_val:
            j -= 1

        if i < j:
            a[i], a[j] = a[j],a[i]

    a[srt],a[j] = a[j],a[srt]
    return j

a = [9,2,4,7,3,8,5]
QuickSort(a,0,len(a) - 1)
print(a)

    