"""Practical: 2.8 String Methods Practice"""

sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Stripped:", sentence.strip())
print("Words list:", sentence.split())
print("Spaces replaced:", sentence.replace(" ", "_"))
print('First occurrence of "a":', sentence.find("a"))
