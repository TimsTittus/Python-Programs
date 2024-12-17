import string

password = input("Enter your password : ")
complexity = 0

if len(password) >= 8:
    complexity += 1

if any(char.isupper() for char in password):
    complexity += 1

if any(char.islower() for char in password):
    complexity += 1

if any(char.isdigit() for char in password):
    complexity += 1

special_characters = string.punctuation
if any(char in special_characters for char in password):
    complexity += 1

print("Password complexity score : ",complexity)

if complexity < 3:
    print("Weak Password!")
elif complexity == 3:
    print("Moderate Password!")
else:
    print("Strong Password!")
