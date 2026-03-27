class Student :
    school = "Bansal institute of enginnering collage"

    def __init__(self, name , marks , attendense):
        self.name = name
        self.marks = marks
        self.attendense = attendense

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >=75:
            return "B"
        else:
            return "C"

s1 = Student("shivam", 98, "100%")
print(s1.calculate_grade())
print(s1.attendense)