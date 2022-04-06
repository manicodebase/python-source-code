import os
import sys

def checkstringreverse(mystring):
    # return mystring[::-1]
    if len(mystring) == 0:
        return 
    temp = mystring[0]
    checkstringreverse(mystring[1:])
    print(temp,  end="")

def removeConsecutiveDuplicates(mystring):
    if (len(mystring) < 2):
        return mystring
    if (mystring[0] != mystring[1]): # M and o
        return mystring[0]+removeConsecutiveDuplicates(mystring[1:]) # return M
        
    # return removeConsecutiveDuplicates(mystring[1:])


baseString = "Moon"
# finalValue = checkstringreverse(baseString)
value = removeConsecutiveDuplicates(baseString)
print (value)
