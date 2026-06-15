def MergeSort(l,left,right):

    if right - left <= 1:
        return(l[left:right])
    
    if right - left > 1:
        mid = (left + right) // 2

        L = MergeSort(l,left,mid)
        R = MergeSort(l,mid,right)
        
    return(merge(L,R))

def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)

    while i+j < m+n:
        if i == m:
            C.append(B[j])
            j = j+1

        elif j == n:
            C.append(A[i])
            i += 1

        elif A[i] <= B[j] :
            C.append(A[i])
            i += 1  

        elif B[j] < A[i]:
            C.append(B[j])
            j = j+1
    return C

a = [9,8,7,6,5,4,0,3,2,1]
print(MergeSort(a,0,len(a)))