class Member:
    def __init__(self, fullname):
        self.fullname = fullname

    def member(self):
        print(f"Hi, my name is {self.fullname}")

class Student(Member):
    def __init__(self, reason, fullname):
        super().__init__(fullname)
        self.reason = reason
        
class Instructor(Member):
    def __init__(self, fullname, bio, skills, add_skill):
        super().__init__(fullname)
        self.bio = bio
        self.skills = skills
        self.add_skill
        
class Workshops():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.student = []
        self.instructor = []
        
    