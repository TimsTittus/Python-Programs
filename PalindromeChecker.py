# Get user input
word = input("Enter a word to check if it's a palindrome: ")

# Check if the word is the same when reversed
if word == word[::-1]:
    print(f'"{word}" is a palindrome!')
else:
    print(f'"{word}" is not a palindrome.')
