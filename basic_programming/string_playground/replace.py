
def replace_string(mystring):
    return mystring.replace("()", "o").replace("(al)", "al")

# data = "G()(al)" #output Goal
# output = replace_string(data)


def path_finder(mylist):
    my_dict = {}
    for path in mylist:
        city_a, city_b = path
        my_dict[city_a] = my_dict.get(city_a, 0) + 1
        my_dict[city_b] = my_dict.get(city_b, 0)
    for city_name, city_value in my_dict.items():
        if (city_value == 0):
            return city_name
        


data = [["B", "C"], ["D", "B"], ["C", "A"]] #output A as A is the destination ciity
last_node = path_finder(data)
print (last_node)
