'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
def CountString(s,word):
    count = 0
    sLength = len(s)
    wordLength = len(word)
    if s == '':
        print("Number of times bob occurs is: ",count)
    else:
        for i in range(sLength):
            if s[i:i+3] == word:
                print(count, " ",s[i:wordLength] )
                count += 1
                wordLength += 1
            else:
                wordLength += 1
    print("Number of times bob occurs is: ",count)

#s = 'azcbobobegghakl'
s = 'bobobobobobobobobobob'
word = 'bob'
CountString(s,word)