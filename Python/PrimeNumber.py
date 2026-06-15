def primeNumbers(n):
    if n > 3 and n % 2 == 0 or n % 3 == 0:
        return("Not a prime number")
    
    else:
        i = 5
        while i*i <= n:
            if n % i == 0 or n % i+2 == 0:
                return("Not a prime number")
            i += 6
        return("Its a prime number")
    
print(primeNumbers(29))
