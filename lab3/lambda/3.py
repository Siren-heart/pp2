numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

names = ["Alice", "Bob", "Amanda", "Charlie"]
a_names = list(filter(lambda name: name.startswith('A'), names))
print(f"Names starting with 'A': {a_names}")