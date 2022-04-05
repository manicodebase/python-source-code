class checknumbergame:
    def __init__(self, number):
        self.number = number 
    
    def palindrome(self):
        n = self.number
        rev = 0
        while self.number != 0:
            digit = self.number % 10 # 3
            rev = rev * 10 + digit
            self.number = self.number // 10 # 12
        print(rev)
        if (n == rev):
            print ("Number is Plaindrome")
        else:
            print ("Number is not palindrome")
    
    

a = checknumbergame(121)
a.palindrome()
a = checknumbergame(123)
a.palindrome()