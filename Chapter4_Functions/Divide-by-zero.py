def spam(divideBy):
    try:
        #Any code in this block that causes ZeroDivisionError wont crash the program
        return 42 / divideBy
    except ZeroDivisionError:
        # If ZeroDivsion Error Happened, the code in this block runs:
        print("ErrorL: Invalid argument")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
