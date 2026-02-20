def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(f"Musician: {musician}")

def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([10, 5, 20, 2])
print(f"Min: {min_val}, Max: {max_val}")