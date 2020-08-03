x = 27
epsilon = 0.01
guess = 0
low = 0.0
high = x
ans = (low + high)/2.0
while abs(ans ** 3 - x) >= epsilon:
    print("Low: ", low, " High: ", high)
    if ans ** 3 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
    guess += 1
print("Number Of Guesses: ", guess, " Guess: ", ans)