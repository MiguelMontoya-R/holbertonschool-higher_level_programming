def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list.copy()
        if idx >= 0 and idx < len(my_list):
            new_list[idx] = element
            return new_list
        else:
            return new_list
