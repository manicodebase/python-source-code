class comprehension:
    def __init__(self, mylist):
        self.mylist = mylist

    def list_out(self):
        out_list = [x*2  if x <= 2 else x * 3 for x in self.mylist ]
        print(out_list)

    def string_manipulation(self):
        myvalue = sum ([self.mylist.count(i) %2  for i in set(self.mylist)]) <= 1
        print(myvalue)
        # mydict = {}
        # print (self.mylist.count('a') for x in self.mylist if x== 'a') #count repeted element in str\
        # print (self.mylist.count('e'))

    def remove_vowels(self):
        vlist = ['a', 'e', 'i', 'o', 'u']
        value = [self.mylist.replace(i, "") if i in vlist else i for i in self.mylist]
        print (value)




# base_list = [4,5,6,3,2,1]
# base_str  = "abbabaacb"
# list_obj1 = comprehension(base_str)
# list_obj1.remove_vowels()

def just_string_change(mylist):
    myspace = ""
    for i in mylist:
        myspace =  myspace+i 
    return myspace

    # return i
data = ["A", "M", "I", "T"]
output_str = just_string_change(data)
print (output_str)