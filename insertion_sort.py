#################################################
#            insertion sort                     #
#################################################
# If left key is larger then the right one,     #
# right shift the key by 1 (A[i+1] = A[i])      #
#                                               #
# The performance of insertion sort is O(n2)    #
#                                               #
#                                               #
#################################################

def swap(l, i, j):
    temp = l[j]
    l[j] = l[i]
    l[i] = temp

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = key




