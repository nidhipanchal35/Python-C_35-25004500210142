"""Practical: 2.9 Anagram Checker"""

def is_anagram(s1, s2):
    clean1 = sorted(s1.replace(" ", "").lower())
    clean2 = sorted(s2.replace(" ", "").lower())
    return clean1 == clean2

pairs = [("listen", "silent"), ("earth", "heart"), ("hello", "world"), ("night", "thing")]
for first, second in pairs:
    print(f"{first!r} and {second!r}: {is_anagram(first, second)}")
