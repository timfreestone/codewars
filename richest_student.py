
# Codewars - this class already existed
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
    max_value = max(student_money.values())

    winners = [
        name for name, value in student_money.items()
        if value == max_value
    ]

    if len(winners) == 1:
        return winners[0]
    else:
        return "all"

students = [
    Student("Alice", 2, 1, 0),
    Student("Bob", 0, 0, 3),
    Student("Charlie", 3, 0, 0),
    Student("Tim", 0, 0, 2)
]
