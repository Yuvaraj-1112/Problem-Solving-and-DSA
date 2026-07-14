def BinarySearch(l1,t):
    l = 0
    r = len(l1) - 1

    while l <= r:
        mid = r+l//2

        if t == l1[mid]:
            print(mid)
            break

        if t < l1[mid]:
            r = mid - 1

        if t > l1[mid]:
            l = mid + 1


li = [1,2,3,4,5,6,7]
t = 6
BinarySearch(li,t)