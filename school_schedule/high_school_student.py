from student import Student

class HighSchoolStudent(Student):
    def __init__(self, name, grade, classes,has_parking_privileges=False,clubs=None):
        super().__init__(name, grade, classes)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = clubs if clubs is not None else []
    
    def join_club(self,club_name):
        self.clubs.append(club_name)
    
    def display_clubs(self):
        club_str = ", ".join(self.clubs)
        if club_str:
            return f"{self.name} is a member of: {club_str}."
        return f"{self.name} didn't join any club."
    
    def display_parking_messages(self):
        has_message = "has" if self.has_parking_privileges else "doesn't have"
        return f"{self.name} {has_message} parking privileges."
    
    def summary(self):
        student_summary = super().summary()
        return student_summary + self.display_clubs() + self.display_parking_messages()





name = "Ellis"
grade = "jonior"
classes = ["Painting"]

ellis = HighSchoolStudent(name,grade,classes)

print(ellis)
print(ellis.summary())
