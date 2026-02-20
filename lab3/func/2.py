def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("hamster", "Harry")

def describe_dog(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_dog("Willie")

def print_models(unprinted_designs):
    for design in unprinted_designs:
        print(f"Printing model: {design}")

designs = ['phone case', 'robot pendant', 'dodecahedron']
print_models(designs)