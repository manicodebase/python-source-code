#findout number of three element whose sum is "0" 


def three_sum(mylist):
    sorted_list = sorted(set(mylist))
    len_of_list = len(sorted_list)
    j = 1
    k= len_of_list - 1
    new_list = []
    for val in range(len_of_list):

        # print (sorted_list[val])
        sum = sorted_list[val] + sorted_list[j] + sorted_list[k]
        # print (sum)
        if sum == 0:
            new_list.append(sorted_list[val]) 
            new_list.append(sorted_list[j])
            new_list.append(sorted_list[k])
        elif sum > 0:
            k -= 1
        else:
            j += 1

    print (new_list)


# data = [-1, 0, 1,2, -1, -4] #[-4, -1, 0, 1, 2]
data = [-1, 0, 1, -2, 5, -3]
three_sum(data)