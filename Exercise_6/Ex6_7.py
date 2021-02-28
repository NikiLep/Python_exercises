# File:         Ex6_7
# Author:       Niki Leppänen
# Description:  Inherit a student and teacher from a participant of OOP course.
#               Think a few proper data attributes that are 1) common for both teachers and students and
#               2) different between teachers and students.

class Course:
    def __init__(self):
        self.__ID = 0
        self.__name = ""

    def set_id(self, id):
        self.__ID = id

    def set_c_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__ID

    def get_c_name(self):
        return self.__name

    def __str__(self):
        return f"""Course name: {self.__name}\nID: {self.__ID}"""


class Teacher(Course):

    def __init__(self):
        Course.__init__(self)
        self.__fname = ""
        self.__lname = ""
        self.__subject = ""

    def set_fname(self, f):
        self.__fname = f

    def set_lname(self, l):
        self.__lname = l

    def set_subject(self, subject):
        self.__subject = subject

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_subject(self):
        return self.__subject

    def __str__(self):
        return f"""\nName: {self.__fname} {self.__lname}\nSubject: {self.__subject}"""


class Student(Course):

    def __init__(self):
        Course.__init__(self)
        self.__fname = ""
        self.__lname = ""
        self.__tasks = 0

    def set_fname(self, f):
        self.__fname = f

    def set_lname(self, l):
        self.__lname = l

    def set_task(self, tasks):
        self.__tasks = tasks

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_subject(self):
        return self.__tasks

    def __str__(self):
        return f"""\nName: {self.__fname} {self.__lname}\nTasks done: {self.__tasks}"""


def main():
    student = Student()
    teacher = Teacher()
    course = Course

    student.set_c_name(input("What course: "))
    student.set_id(int(input("Course id: ")))

    print("\nImput student information")
    student.set_fname(input("Give first name: "))
    student.set_lname(input("Give last name: "))
    student.set_task(int(input("How many tasks done: ")))


    print("\nInput teacher information")
    teacher.set_fname(input("Give first name: "))
    teacher.set_lname(input("Give last name: "))
    teacher.set_subject(input("What subject: "))

    print("Course: ", student.get_c_name(), "ID: ", student.get_id())
    print(student)
    print(teacher)


main()