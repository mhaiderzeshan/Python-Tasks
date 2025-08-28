"""
Count character frequencies in a string and store them in a dictionary, sorted alphabetically by character.
"""

user_string = input("Enter a string: ").lower()
my_string = user_string.replace(" ", "")

freq = {}
for c in my_string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
sorted_dict = sorted(freq.items())
print(sorted_dict)
