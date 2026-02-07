class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show_details(self):
        print(self.name, self.roll_no)

s1 = Student("Nick", 101)
s1.show_details()
