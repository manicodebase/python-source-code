import math 

class arrayExplore:
    def __init__(self, myarray1, myarray2):
        self.myarray1 = myarray1
        self.myarray2 = myarray2

    def median(self):
        [self.myarray1.append(i) for i in self.myarray2]
        sort_list = sum(sorted(self.myarray1)) / len(self.myarray1)
        print (math.modf(sort_list))



data_array1 = [1, 2]
data_array2 = [3,4]

c1 = arrayExplore(data_array1, data_array2)
c1.median()