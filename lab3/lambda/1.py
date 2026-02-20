add_ten = lambda a: a + 10
print(f"Adding 10 to 5: {add_ten(5)}")

multiply = lambda a, b: a * b
print(f"Multiplying 5 and 6: {multiply(5, 6)}")

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(f"Doubling 11: {mydoubler(11)}")