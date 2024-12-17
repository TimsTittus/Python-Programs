def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

number = float(input("Enter a number: "))
check_number(number)
