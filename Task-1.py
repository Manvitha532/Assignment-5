students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
name = input("Enter the student's name: ")

# Checking and displaying result
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
