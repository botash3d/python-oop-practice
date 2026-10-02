class Student:
    def __init__(self,name:str,marks:list[int]=list()):
        self.name=name
        self.marks=marks

    def add_mark(self,m:int):
        self.marks.append(m)

    def average(self):
        return 0 if not self.marks else sum(self.marks)/len(self.marks)

    def __str__(self):
        return f"""Total marks of {self.name} is: {sum(self.marks)}
Average Marks of {self.name} is : {round(self.average())}
"""

student1=Student("Ashwani",[70,90,60])
student2=Student("Aman",[])
print(student1)
print(student2)