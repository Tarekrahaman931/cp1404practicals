"""
CP1404/CP5632 Practical
Word Occurrences Counter
Estimate: 20 minutes
"""

# Get the input text from the user
text = input("Text: ")

# Split the text into words and count the occurrences using a dictionary
word_count = {}
words = text.split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Find the longest word for formatting purposes
longest_word_length = max(len(word) for word in word_count)

# Sort the dictionary by the words (keys) and print the results
for word in sorted(word_count):
    print(f"{word:{longest_word_length}} : {word_count[word]}")
