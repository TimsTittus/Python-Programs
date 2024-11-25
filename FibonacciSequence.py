# Fibonacci Sequence Program

# Input: number of terms
num_terms = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

# Check if the number of terms is valid
if num_terms <= 0:
    print("Please enter a positive number.")
elif num_terms == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    for _ in range(num_terms):
        print(a, end=" ")  # Print the current term
        a, b = b, a + b    # Update to the next terms