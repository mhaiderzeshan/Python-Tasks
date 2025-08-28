"""
Write a program that finds the most frequent word in a given paragraph,ignoring punctuation and case.
"""

import string
from collections import defaultdict

user_input = input("Enter the paragraph: ").lower()

translator = str.maketrans('', '', string.punctuation)
clean_text = user_input.translate(translator)
word_list = clean_text.split()

freq = defaultdict(int)
for word in word_list:
    freq[word] += 1

max_freq = max(freq.values())
most_frequent_words = [word for word,
                       count in freq.items() if count == max_freq]

if len(most_frequent_words) == 1:
    print(
        f"The most frequent word is '{most_frequent_words[0]}' (appeared {max_freq} times).")
else:
    words_str = "', '".join(most_frequent_words)
    print(
        f"The most frequent words are '{words_str}' (each appeared {max_freq} times).")
