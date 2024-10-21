import string
import re

# Open the file using the absolute path
with open("/Users/andreneptunejr/DSS522_PE02/poem.txt", "r") as file:
    text = file.read()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split text into words and preserve spaces
words = re.split(r'(\W+)', text.lower())

# Debugging: Print the split words
print(f"Split words: {words}")

# Initialize word count dictionary
word_count = {}

# Count words
for word in words:
    if word.strip() and word not in string.whitespace:  # Skip empty or whitespace-only strings
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Debugging: Print word count
print(f"Word count: {word_count}")

# Find and remove the most frequent word(s)
if word_count:  # Check if word_count is not empty
    max_frequency = max(word_count.values())
    most_frequent_words = [word for word, count in word_count.items() if count == max_frequency]

    for word in most_frequent_words:
        del word_count[word]
else:
    print("No words were counted. Check your input or splitting logic.")

# Output the final word count after removing the most frequent word(s)
print("Final word count after removing most frequent word(s):", word_count)
