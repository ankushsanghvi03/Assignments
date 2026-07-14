def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

text = input("Enter a string:")
print("Number of Vowels:",count_vowels(text))
