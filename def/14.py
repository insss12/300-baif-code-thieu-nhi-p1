def tim_max(list):
    max_list = list[0]
    for num in list:
        if num > max_list:
            max_list = num
    return max_list

