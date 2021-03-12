class Student:
    def __init__(self, scores = []):
        self.scores = scores

    def avg(self):
        return round(sum(self.scores) / len(self.scores))
        
    @staticmethod
    def notice():
        return "Exams next week!"

# kingsley = Student(scores = [3,4,5,6,8])

print(Student.notice())

