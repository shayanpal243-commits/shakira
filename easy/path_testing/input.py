b = int(input("Enter a number: "))

if b > 0:
    print("Positive")
    EXECUTED_PATH.append("Positive") # type: ignore

elif b < 0:
    print("Negative")
    EXECUTED_PATH.append("Negative") # type: ignore

else:
    print("Zero")
    EXECUTED_PATH.append("Zero") # type: ignore

print("Program Finished")