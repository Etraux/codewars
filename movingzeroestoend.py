def move_zeros(lst):
    zero_arr = []
    non_zero_arr = []
    arr_length = len(lst)
    for i in range(arr_length):
        if lst[i] != 0:
            non_zero_arr.append(lst[i])
        else:
            zero_arr.append(lst[i])
    lst = non_zero_arr + zero_arr
  
    return lst