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

    def removeConsecutiveDuplicates(self):
        base_string = self.input_str
        lenght_of_string = len(base_string)
        if lenght_of_string < 2:
            print (f"Output string is {base_string}")
        if base_string[0] != base_string[1]:
            print (f"Output string is {base_string}")
        mystrlist = []
        i = 0
        while lenght_of_string > 0: # 4  Moon
        # for i in range(lenght_of_string):
            if base_string[lenght_of_string-1] == base_string[lenght_of_string-2]:
                mystrlist.append(base_string[lenght_of_string - 2])
            else:
                mystrlist.append(base_string[lenght_of_string -1])
            lenght_of_string = len(base_string[:lenght_of_string - 1])
        print (f"MY list is {(mystrlist)}")
        # print(base_string[1:])
        # # return removeConsecutiveDuplicates(base_string[1:])
        



    
    
# my_input = "Great Country is India"
rev_string = "Moon"
# a = playstringarena(my_input)
b = playstringarena(rev_string)
# b.string_palindrome()
b.removeConsecutiveDuplicates()
# a.find_dup_char()