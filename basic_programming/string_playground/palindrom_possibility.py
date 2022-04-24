import os
import sys
import re

#Print out all possible palindrom from string for example: geeks ==> Two possibilities 
# 1. g e e k s
# 2. g ee k s
def check_possible_palindrom(stringfeed):
    print([stringfeed.count(i) for i in set(stringfeed)])

def find_all_possible_substr(datafeed):
    possible_str = [datafeed[i:j] for i in range(len(datafeed)) for j in range(i+1, len(datafeed)+ 1 )]
    print (possible_str)
    # explored below
    # for i in range(len(datafeed)): 
    #     for j in range(i+1, len(datafeed) +1):
    #         print (i, j)
    #         print (datafeed[i:j])
mystring = "aabbc"
# check_possible_palindrom(mystring)
find_all_possible_substr(mystring)