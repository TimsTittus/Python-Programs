# Multiplication Table

number = int(input("Enter a number: "))

print(f"Multiplication Table for {number}:")
for i in range(1, 11):  # Loop from 1 to 10
    result = number * i
    print(f"{number} x {i} = {result}")