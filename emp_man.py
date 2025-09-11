class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print(f"the employee name is  {self.name} and {self.sal}")
class Manager(Employee):
    def __init__(self,name,sal,department):
        super().__init__(name,sal)
        self.department=department
    def display(self):
        # super().display() 
        print( f"{self.name}  {self.sal}  {self.department}")
       

obj=Employee("rav",45)
obj.display()
obj1=Manager("pav",78,"csd")
obj1.display()

