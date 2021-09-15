#!/usr/bin/python3
def weight_average(my_list=[]):

    if my_list == []:
        return 0

    sum = 0
    divisor = 0

    for i, j in my_list:

        sum += (lambda i, j: i * j)(i, j)

    for i in my_list:
        divisor += i[1]

    return(sum/divisor)
