#Find out all possible subsutring combination'
class substringSolution:
    def __init__(self, mystring):
        self.mystring = mystring
    
    def possible_substr(self):
        # for i in range(len(self.mystring)):
        #     for j in range(i+1, len(self.mystring)+1):
        #         print (self.mystring[i:j])

        # List Comprehension
        value = [self.mystring[i:j] for i in range(len(self.mystring)) for j in range(i+1, len(self.mystring)+1)]
        print (value)
        # return value

data = "abcde"
instace_one = substringSolution(data)
instace_one.possible_substr()