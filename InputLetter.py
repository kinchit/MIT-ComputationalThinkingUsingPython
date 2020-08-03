low = 0
high = 100
guess = 100
#print("Please think of a number between 0 and 100!")
guessed = False
print("Is your secret number ",guess, "?")
#ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while not guessed:
    print("Is your secret number ",guess, "?")
    guess = (high + low)//2
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if(ans == 'h' or ans == 'l' or ans == 'c'):
        if (ans == 'h'):
            high = guess
        elif (ans == 'l'):
            low = guess
        elif ans == 'c':
            guessed = True
print("Game over. Your secret number was: ",ans)