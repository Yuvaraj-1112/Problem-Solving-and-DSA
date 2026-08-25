def linearSearch(l,v):

    i = 0
    pos = -1
    for x in l:
        if x == v:
            pos = i
        i += 1
    return(pos)

a = [1,5,7,3,6,9]
b=9

print(linearSearch(a,b))
    
    
