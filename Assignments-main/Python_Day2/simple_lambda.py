add = lambda x,y: x + y
print(add(5, 3))

find_largest_word = lambda sentence: max(sentence.split(), key=len)
sentence = input("Enter a sentence: ")
largest_word = find_largest_word(sentence)
print("Largest word: ", largest_word)
print("Length: ", len(largest_word))

"""hello"""
