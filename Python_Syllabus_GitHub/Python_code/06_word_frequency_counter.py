"""Practical: 3.6 Word Frequency Counter"""

import re
from collections import Counter

paragraph = input("Enter a paragraph: ")
words = re.findall(r"\b[\w']+\b", paragraph.lower())
frequency = Counter(words)
print("Words sorted by frequency (most common first):")
for word, count in sorted(frequency.items(), key=lambda item: (-item[1], item[0])):
    print(f"{word}: {count}")
