numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")

words = ["python", "is", "awesome"]
upper_words = list(map(lambda w: w.upper(), words))
print(f"Uppercase: {upper_words}")