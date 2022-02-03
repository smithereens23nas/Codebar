from operator import indexOf


class Member:
    def __init__(self, fullname):
        self.fullname = fullname

    def member(self):
        print(f"Hi, my name is {self.fullname}")

class Student(Member):
    def __init__(self, fullname, reason):
        super().__init__(fullname)
        self.reason = reason
        
class Instructor(Member):
    def __init__(self, fullname, bio):
        super().__init__(fullname)
        self.bio = bio
        self.skills = ''
        
    def add_skill(self, skill):
        # self.skills.append(skill)
        self.skills += skill
        
class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.student = []
        self.instructor = []
        
    def add_participant(self, member):
        self.member = member
        if(type(member).__name__) == 'Student':
            self.student.append(member)
        elif(type(member).__name__) == "Instructor":
            self.instructor.append(member)
        else:
            print('member does not exist')
            
    
    def print_details(self):
        print(f"Workshop details: {self.date}, {self.subject}")
        for idx, student in enumerate(self.student):
            print(f"{idx + 1}. {student.fullname} - {student.reason}")
        print("Instructors") 
        for idx, instructor in enumerate(self.instructor):
            skills = []
            skills.append({instructor.skills})
            print(f"{idx + 1}. {instructor.fullname} - {instructor.skills} - {instructor.bio}")

    
workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
