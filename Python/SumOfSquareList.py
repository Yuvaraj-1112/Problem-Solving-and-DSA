def sumsquare(l):
    even = 0
    odd = 0
    for x in l:
        if x % 2 == 0:
            even += x * x
        
        else:
            odd += x * x

      
    return [odd, even]

l1 = [1,2,3,4,5,6]
print(sumsquare(l1))