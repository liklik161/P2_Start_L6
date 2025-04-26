from student import Student

class klaslokaal:
    def __init__(self):
        self.naam = []
    def voeg_student_toe(self, namen):
        self.naam.append(namen)
    def toon_studenten(self):
        for studenten in self.naam:
            studenten.stel_voor()


klaslokaal = klaslokaal()
student1 = Student("dries","15")
student2 = Student("Ron","16")
klaslokaal.voeg_student_toe(student1)
klaslokaal.voeg_student_toe(student2)
klaslokaal.toon_studenten()

