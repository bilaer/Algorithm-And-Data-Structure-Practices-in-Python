##########################################
#
#
#
#
#
#########################################

import math
from insertion_sort import insertion_sort


def bucket_sort(l):
    temp = []
    for _ in range(len(l)):
        temp.append([])
    result = [0]*len(l)
    # Put items into the buckets
    for i in range(len(l)):
        print("temp len: %d\n" %(len(temp)))
        print("index: %d\n" %(math.ceil(len(l)*l[i]) - 1))
        temp[math.ceil(len(l)*l[i]) - 1].append(l[i])
    # Sort the lists inside the bucket (insertion sort)
    for i in range(len(l)):
        if len(temp[i]) != 0:
            insertion_sort(temp[i])
    # Finally concatenate all the lists temp[0], temp[1]...
    for i in range(len(l)):
        if len(temp[i]) != 0:
            result = result + temp[i]
    return result

list = [1,5,3,5,3,6,3]
bucket_sort(list)
print(list)
