def find_longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    print("Longest Words:", longest)
    print("Length:", len(longest))

sentence = input("Enter a sentence: ")
find_longest_word(sentence)