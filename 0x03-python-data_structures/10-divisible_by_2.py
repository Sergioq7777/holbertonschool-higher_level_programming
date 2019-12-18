#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = list.copy(my_list)
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            lst[i] = 1
        elif (my_list[i] % 2 != 0):
            lst[i] = 0
    return(lst)
