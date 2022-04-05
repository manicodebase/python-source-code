class playstringarena:
    def __init__(self, input_str):
        self.input_str = input_str 
    
    def find_dup_char(self):
        duplicates = {}
        for i in self.input_str:
            if i in duplicates:
                duplicates[i] += 1
            else:
                duplicates[i] = 1
        for k, v in duplicates.items():
            if (v > 1):
                print (k)
    
    def string_palindrome(self):
        str = ""
        for i in self.input_str:
            str = i + str # Reversal of String
        if (self.input_str == str):
            print("String is palindrome")
        else:
            print ("String is not palindrome")
    
    
# my_input = "Great Country is India"
rev_string = "Moon"
# a = playstringarena(my_input)
b = playstringarena(rev_string)
b.string_palindrome()
# a.find_dup_char()