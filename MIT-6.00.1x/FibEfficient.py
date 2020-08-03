def fibEfficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fibEfficient(n-1,d) + fibEfficient(n-2,d)
        d[n] = ans
        return ans

dict = {1:1,2:2}
print(fibEfficient(5,dict))