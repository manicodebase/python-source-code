class checkteenager:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def count_age(self):
        if self.age < 20:
            print (f"{self.name} is Teenager")
        else:
            print (f"{self.name} Geeting mature now")

class babies(checkteenager):
    def __init__(self, name, age, father_name, salary):
        self.father_name = father_name
        self.salary = salary
        # checkteenager.__init__(self, name, age)
        super().__init__(name, age) # above statemen and this statement is same. it has two methid isinstanceof() and issubclass()
    
    def babies_status(self):
        if self.age < 8:
            if self.salary > 200000:
                print (f"Baby {self.name} is in good hand")
        else:
            print (f"{self.name} should try to earn")
    

a = babies("sachin", 21, "mani", 300000)
a.babies_status()
b = checkteenager("sachin", 21)
b.count_age()