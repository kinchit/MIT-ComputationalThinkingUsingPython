'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''

def CountVowels(s):
    count = 0
    vowels = 'aeiou'
    if s == '':
        return 0
    else:
        for ch in s:
            if ch in vowels:
                count += 1
    return count

s = 'azcbobobegghakl'
#s = 'zbc'
print(CountVowels(s))