def isValid(alist):
    temp = alist[:]
    temp.reverse()
    if temp == alist:
        return True
    else:
        return False


def isPoly():
    word = []
    num = int(input("Enter the number of characters: "))
    for i in range(num):
        ch = input("Enter Charater for word: ")
        word.append(ch)
    print(word)
    if isValid(word):
        return "Yes"
    else:
        return "No"
    
print(isPoly())