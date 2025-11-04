#data-set we are using
students = [
    {"name": "Yohan", "marks": 85},
    {"name": "Madhav", "marks": 74},
    {"name": "Bala", "marks": 92},
    {"name": "Anu", "marks": 68}
]

#1. print all students names
print("The students")
for s in students:
    print(s["name"])

#2. calculate average marks
avg_marks = sum(s["marks"] for s in students) / len(students)
print(f"Average marks:{avg_marks}")

#3. Find the topper
topper = max(students, key=lambda x: x["marks"])
print(f"Topper:{topper["name"]}")