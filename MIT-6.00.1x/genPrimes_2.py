def genPrimes():
    
    primes = [ 2, 3, 5, 7, 11 ]
    
    def isPrimeNumber(n):
        if n in primes:
            return True
        
        for elem in primes:
            if n % elem == 0:
                return False
                
        primes.append(n)
        return True
        
    ####
    
    num = 1
    
    while True:
        num += 1
        if isPrimeNumber(num):
            next = num
            yield next
            #num = next
    ####
####
            
            
primeNumber = genPrimes()

for i in range(10):
    print(primeNumber.__next__())