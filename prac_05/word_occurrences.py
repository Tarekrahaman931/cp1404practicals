"""
Time estimate: 20 minutes
"""

input_string = input("Enter a string: ")

words = input_string.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_length = max(len(word) for word in word_counts.keys())

sorted_word_counts = sorted(word_counts.items())

for word, count in sorted_word_counts:
    print(f"{word:>{max_length}} : {count}")
