# s = 'abcbc'
# current = ''
# longest = ''
# for i in range(len(s)):
#  if (s[i] >= s[i-1]):
#   current += s[i]
#  else:
#   current = s[i]
#  if len(current) > len(longest):
#   longest = current
# print("Longest substring in alphabetical order is: " + longest)

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))