class checkteenager:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def count_age(self):
        if self.age < 20:
            print (f"{self.name} is Teenager")
        else:
            print (f"{self.name} Geeting mature now")

a = checkteenager("sachin", 19)
a.count_age()