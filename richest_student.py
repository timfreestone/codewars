class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


# ok this works for the final row (Charlie), but what happened to the others? need to append
def most_money(students):
    student_money = {}
    for student in students:
        student_money[student.name] = (student.fives * 5 + student.tens * 10 + student.twenties * 20)
    return student_money



students = [
    Student("Alice", 2, 1, 0),
    Student("Bob", 0, 0, 2),
    Student("Charlie", 4, 0, 0)
]

print(most_money(students))