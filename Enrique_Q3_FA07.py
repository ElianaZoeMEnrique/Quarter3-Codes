students = []

for i in range(3):
    student = {}

    student["name"] = input("Enter name: ")
    student["age"] = int(input("Enter age: "))
    student["grade"] = int(input("Enter grade: "))

    students.append(student)
    print()

print("Class Directory:")

for s in students:
    print(f"{s['name']} | Age: {s['age']} | Grade: {s['grade']}")