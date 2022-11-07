# Create tuples of students (Name, Grade, Age)
student_tuples = [
('John', 'A', 12),
('Zaid', 'B', 15),
('Dave', 'B', 10),
]

# Sort tuples by name (index 0)
sorted_students = sorted(student_tuples, key=lambda student:student[0])
print(sorted_students)

# Sort tuples by age (index 2)
sorted_students = sorted(student_tuples, key=lambda student:student[2])
print(sorted_students)

# Sort tuples reversed by age
sorted_students = sorted(student_tuples, key=lambda student:student[2], reverse = True)
print(sorted_students)
