# Iterative Apprach
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    min = 0
    if a < b:
        min = a
        max = b
    else:
        min = b
        max = a
    for i in range(min,0,-1):
        if (max%i == 0 and min%i == 0):
            return i

#Recursive Approach
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)

print(gcdRecur(6,12))
