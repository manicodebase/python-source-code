#sorting is different parameter
from audioop import reverse


class sortingMech:
    def __init__(self, mylist):
        self.mylist = mylist
    
    def sorting_versions(self):
        versions_list = self.mylist
        # versions_list.sort(key=lambda s: map(s.split('.')))
        # print(versions_list)
        # fist_ver = []
        for i in versions_list:
            print (i)
            for j in i.split('.'):
                print (list(tuple(j)))
    
mydata = ["1.12.0", "1.2.1",  "12.0.3",  "1.13.13",  "9.0.29"]
# mydata= ['version-1.9', 'version-2.0', 'version-1.11', 'version-1.10']
c1 = sortingMech(mydata)
c1.sorting_versions()
