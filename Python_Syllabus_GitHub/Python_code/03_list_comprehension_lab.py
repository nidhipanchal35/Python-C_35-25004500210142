"""Practical: 3.3 List Comprehension Lab"""

squares = [n ** 2 for n in range(1, 21)]
evens = [n for n in range(1, 51) if n % 2 == 0]
sentence = input("Enter a sentence: ")
long_words = [word for word in sentence.split() if len(word) > 4]
odd_cubes = [n ** 3 for n in range(1, 16) if n % 2 == 1]
print("Squares 1-20:", squares)
print("Even numbers 1-50:", evens)
print("Words longer than 4 characters:", long_words)
print("Cubes of odd numbers 1-15:", odd_cubes)
