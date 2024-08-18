class person():
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def display(self):
            print(f"name:{self.name}")
            print(f"age: {self.age}")
class student(person):
    def __init__(self,name, age,section):
         super().__init__(name, age)
         self.section=section
    def displayStudent(self):
        print(f"name:{self.name}")
        print(f"age: {self.age}")
        print(f"section: {self.section}")
             
s1=student("emad medhat",22,1)    
s1.displayStudent()
                