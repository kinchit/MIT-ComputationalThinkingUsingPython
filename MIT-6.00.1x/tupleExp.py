def getData(aTup):
    nums = ()
    words = ()
    for t in aTup:
        nums = nums + (t[0],)
        if (t[1] not in words):
            words = words + (t[1],)
    min_num = min(nums)
    max_num = max(nums)
    uniq = len(words)
    #print(words)
    return (min_num, max_num, uniq)

(small,large, uniq) = getData(((1,'mine'),
                       (2,'yours'),
                       (3,'ours'),
                       (4,'mine')))
print(large)