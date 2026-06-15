def remdup(l):
    
    seen = set()
    l2 = []
    for x in l:
        if x not in seen:
            seen.add(x)
            l2.append(x)
        
    return l2

l1 = [3,1,5,3,2]
print(remdup(l1))