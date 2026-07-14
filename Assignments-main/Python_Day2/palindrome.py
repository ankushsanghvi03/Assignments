def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
word = input("Enter a string: ")

if is_palindrome(word):
    print(f'"{word}" is a Palindrome.')
else:
    print(f'"{word}" not a Palindrome.')
