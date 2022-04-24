def sort_list_of_version(mylist):
    final_data = {}
    for value in mylist:
        value = value.split("-")
        final_data[value[1]] = value[0]
    sorted_keys = sorted(final_data)
    print (sorted_keys)





data = ["1.0.0-12", "20.0.0-99", "1.0.0-24", "1.0.1-10", "2.0.0-30", "2.0.0-999", "2.0.1-19"]
sort_list_of_version(data)