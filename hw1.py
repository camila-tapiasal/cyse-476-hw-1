import re
from collections import defaultdict

# Part 1: Word to Patterns

def word_to_pattern(word):
    pattern = []
    mapping = {}
    current = ord('a')
    for i in word.lower():
        if i not in mapping:
            mapping[i] = chr(current)
            current += 1
        pattern.append(mapping[i])
    return ''.join(pattern)

# Part 2: Pattern to Words

def pattern_to_words(pattern, word_list):
    pattern_regex = '^' + pattern.replace('_', '[a-z]') + '$'
    matching_words = [word for word in word_list if re.match(pattern_regex, word)]
    return matching_words

# Utility function to read words from a file
def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return [word.strip() for word in file.readlines()]

# Utility function to write words to a file
def write_words_to_file(words, file_path):
    with open(file_path, 'w') as file:
        for i in words:
            file.write(i + '\n')

if __name__ == "__main__":
    # Sample usage for Part 1
    word = input("Enter a word: ")
    pattern = word_to_pattern(word)
    print(f"The pattern for '{word}' is '{pattern}'")

    # Sample usage for Part 2
    word_list = read_words_from_file("words_alpha.txt")
    pattern = input("Enter a word pattern: ")
    matching_words = pattern_to_words(pattern, word_list)
    print(f"Number of matching words: {len(matching_words)}")
    print("Matching words:")
    for word in matching_words:
        print(word)
