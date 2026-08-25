n = int(input())
a = 0

while n > 0:
    val = n % 10 
    a = (a* 10) + val
    n = n//10

print(a)