# Challenge #3 - Create Student Classes

class Student:
    valid_courses = ["Computer Science", "Software Engineering", "Networks and Security", "Data Science", "Cybersecurity", "Computing"]

    def __init__(self, up_number, course, year):
        self._course = course
        self._up_number = up_number
        self.year = year

    @property
    def course():
        return self._course

    @course.setter
    def course(self, new_course):
        if new_course in self.valid_courses:
            self._course = new_course

    @property
    def up_number(self):
        return self._up_number

    def progress(self):
        if (self.year > 0) and (self.year <= 4):
            self.year += 1

    def __str__(self):
        return f"Student up{self._up_number} studying {self._course} in year {self.year}"


class PlacementStudent(Student):
    def __init__(self, up_number, course, year, company):
        super().__init__(up_number, course, year)
        self.company = company

    def __str__(self):
        if self.year == 3:
            return f"Placement student up{self._up_number} working at {self.company}"
        else:
            return f"Placement student up{self._up_number} studying {self._course} in year {self.year}"


def test_student():
    student1 = Student(2254321, "Computer Science", 2)
    print(student1)
    student1.progress()
    print(student1)
    student1.course = "Software Engineering"
    print(student1)
    student1.progress()
    print(student1)

    student2 = PlacementStudent(26432123, "Networks and Security", 2, "Google")
    print(student2)
    student2.progress()
    print(student2)


test_student()
