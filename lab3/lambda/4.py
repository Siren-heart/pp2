students = [
    {"name": "John", "grade": 88},
    {"name": "Jane", "grade": 92},
    {"name": "Dave", "grade": 85}
]

sorted_by_grade = sorted(students, key=lambda s: s["grade"])
print("Sorted by grade:")
for student in sorted_by_grade:
    print(student)

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(f"\nSorted pairs alphabetically by word: {sorted_pairs}")