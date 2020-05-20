# CLASSES AND OBJECTS IN PYTHON


class Student:

    grace_marks = 10
    number_of_objects = 0

    def __init__(self, name, roll, course, grade):                  # __init__ method is like constructor, it will always have self in its parameter list...
        self.s_name = name                                          # self refers to the current object,it is
        self.s_roll = int(roll)                                     # like this keyword
        self.s_course = course                                      # s_name, s_roll, etc are instance variables
        self.s_grade = grade                                        # name, roll, course are local variables
        Student.number_of_objects += 1

    @classmethod
    def add_grace_marks(cls, new_grace_marks):
        cls.grace_marks = new_grace_marks

    def display_info(self):
        print("Name:", self.s_name)
        print("Course:", self.s_course)
        print("Roll No.:", self.s_roll)
        print("Grade:", self.s_grade)



print(Student.number_of_objects)
student_1 = Student('Manak Upadhyay', 13, 'Computer Science', 89);         # doing this, will invoke the __init__ method...
student_2 = Student("Manu Upadhyay", 14, 'Information Technology', 90);
print(Student.number_of_objects)
student_1.display_info()                                                    # calling the display_info method
# student_2.display_info()
# Student.display_info(student_1)                                              # we can also call the method like this...
    # print(student_2.__dir__())                                # it lists all the attributes and functions associated with an object
# print(Student.grace_marks)
# Student.add_grace_marks(20)
# print(Student.grace_marks)

