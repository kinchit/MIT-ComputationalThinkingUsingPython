try:
    a = int(input("Tell me first number:"))
    b = int(input("Tell me second number:"))
    print(a/b)
    print("Okay")
except ValueError:
    print("Bug in user input")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except:
    print("Exception occured")
print("Outside Try-Except")

