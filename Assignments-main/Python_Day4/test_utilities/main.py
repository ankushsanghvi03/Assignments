class TextUtilities:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())
    
    def unique_words(self, ignore_case=True):
        words = self.text.split()

        if ignore_case:
            words = [word.lower() for word in words]

        return list(set(words))
    
    def reverse_string(self):
        return self.text[::-1]
    
text = input("Enter a sentence: ")

obj = TextUtilities(text)

print("\nOriginal text: ", obj.text)
print("Word count: ", obj.word_count())
print("Unique words: ", obj.unique_words())
print("Reversed string: ", obj.reverse_string())

print("\nCase Sensitive :", list(set(obj.text.split())))
print("Case Insensitive :", obj.unique_words())