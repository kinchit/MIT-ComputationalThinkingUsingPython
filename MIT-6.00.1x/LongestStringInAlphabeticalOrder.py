'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
def AlphabeticalOrder(inputString):
    newSt = s[0]
    maxSt = ''
    if s == '':
        return ''
    for i in range(1,len(s)):
        if ord(s[i]) >= ord(s[i-1]):
            newSt += s[i]
            if len(maxSt) < len(newSt):
                maxSt = newSt
        else:
            newSt = '' + s[i]
#     prevChar = ""
#     currentString = ""
#     longestString = ""
# 
#     for char in inputString:
#         if prevChar <= char:
#             currentString += char
#             if len(currentString) > len(longestString):
#                 longestString = currentString
#         else:
#             currentString = char
#         prevChar = char
#     print('Longest substring in alphabetical order is: ' + longestString )
    print(maxSt)

#s = 'azcbobobegghakl'
#s = 'abcbcd'
s = 'unsnmlwqhswtynkj'
#inputString = 'azcbobobegghakl'
#s = 'qidmqntcqagxm'
AlphabeticalOrder(s)