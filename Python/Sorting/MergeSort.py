def MergeSort(arr,srt,end):

    if end - srt <= 1:
        return
    
    mid = (srt + end) // 2

    MergeSort(arr, srt,mid)
    MergeSort(arr,mid,end)

    return(merge(arr,srt,mid,end))

def merge(arr,srt,mid,end):

    c = []
    (i,j) = (srt,mid)

    while i < mid and j < end:

        if arr[i] <= arr[j]:
            c.append(arr[i])
            i += 1

        else:
            c.append(arr[j])
            j += 1

    while i < mid:
        c.append(arr[i])
        i += 1

    while j < end:
        c.append(arr[j])
        j += 1


    for k in range(len(c)):
        arr[srt + k] = c[k]


    
arr = [ num for num in range(50,0,-1)]

MergeSort(arr,0,len(arr))
print(arr)