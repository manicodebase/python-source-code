import queue


def check_valid_parenthesis(datafeed):
    # value = [datafeed.count(i) %2 != 0 for i in set(datafeed)]
    # print (value)
    if len(datafeed) %2 != 0:
        return "Invalid" 
    # open_braces = ('([{')
    # close_braces = (')]}')
    # my_dict = dict(zip(open_braces, close_braces))
    my_dict = {"(": ")", "[": "]", "{": "}"}
    my_stack = []
    for i in datafeed:
        if i in my_dict.keys(): # open parenthesis
            my_stack.append(i)
        elif my_stack and my_dict[i] == my_stack[-1]:
            my_stack.pop()
        else:
            return "Invalid"
    
    return my_stack

        # else:
        #     if not my_stack:
        #         return "invalid"
        #     # value = my_stack.pop()
        #     elif  i !=  my_dict[my_stack.pop()]:
        #         return "invalid"


    # for i in datafeed:
    #     if i in open_tup:
    #         my_stack.append(i)
    #     if i in close_tup:
    #         if not my_stack:
    #             return "Invalid"
    #         elif (my_stack.pop() != map[i]) :
    #             return "Invalid"
    #         else: 
    #             continue
    # if not my_stack:
    #     return "Valid"
    # else:
    #     return "Invalid"
    # print (my_stack)
        # elif i in close_tup:
        #     if not my_queue or i != my_queue.pop():
        #         return "invalid"
        # if not my_queue:
        #     return "Valid"
        # else:
        #     return "Invalid"
    # print(my_queue)
        

mystr = "()"
check_result = check_valid_parenthesis(mystr)
if not check_result:
    print ("Valid")
else:
    print ("Invalid")

# in case ==> () => should print valid parenthesis
# in case "())" ==> invalid  => to make it correct we need to add anothe "(" so
# ()[]{} => valid 
# (] ==> invalid

