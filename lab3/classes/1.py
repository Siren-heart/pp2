class SimpleClass:
    pass

obj = SimpleClass()
print(f"Created an object: {obj}")

obj.custom_property = "Hello World"
print(f"Property value: {obj.custom_property}")

del obj.custom_property