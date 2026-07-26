b = int(input("Enter a number: "))

if b > 0:
    print("Positive")
    EXECUTED_PATH.append("Positive")

elif b < 0:
    print("Negative")
    EXECUTED_PATH.append("Negative")

else:
    print("Zero")
    EXECUTED_PATH.append("Zero")

print("Program Finished")