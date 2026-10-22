"""Practical: 2.6 Vowel Counter & Character Frequency"""

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

def char_frequency(s):
    frequency = {}
    for char in s:
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(sentence))
print("Character frequency:", char_frequency(sentence))
