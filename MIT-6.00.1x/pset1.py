#Pset-Ex2
# s = 'azcbobobegghakl'
# count = 0
# num = 0
# for c in range(len(s)-2):
#     if(s[num:num+3] == 'bob'):
#         count += 1
#     num += 1
# print("Number of times bob occurs is: ",count)

#Pset-Ex3
#s = 'azcbobobegghakl'
s = 'abcbcd'
longSub = ''
temp = ''
for i in range(len(s)-1):
    if s[i] >= s[i-1]:
        longSub += s[i]
    else:
        if(len(temp) < len(longSub)):
            temp = longSub
        longSub = s[i]
print(temp)