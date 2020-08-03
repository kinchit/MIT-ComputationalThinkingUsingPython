def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

def positive(x):
    return abs(x)

def applyFunc(L,x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

testList = [1, -4, 8, -9]
print(applyToEach(testList,positive))

print(applyFunc([inc, square, halve, abs], -3))