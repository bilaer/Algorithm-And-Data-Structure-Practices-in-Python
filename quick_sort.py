##############################################################
#                        quick sort                          #
##############################################################
#                                                            #
# In quick sort, select one pivot(usually the right end      #
# value of the array as the value to determine the parition  #
# position of the given array. When the parition done,       #
# A[i] <= pivot if i <= p and A[j] >= pivot if j >= p        #
#                                                            #
# The overall performance of quick sort is O(nlgn)           #
# The worse case is when list is divided into                #
# n-1 and 0 elements.                          　　　　　　　　 #
# The best and the average performance of                    #
# quick sort is O(nlgn)                                      #
#                                                            #
##############################################################

# Exchange the values of two places
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

# Partition of the a given list, return the pivot
def partition(l, p, r):
    pivot = l[r]
    index = p
    for i in range(p, r + 1):
        if l[i] < pivot:
            swap(l, i, index)
            index = index + 1
    swap(l, index, r)
    return index

# Quick sort main function
def quicksort_rec(l, p, r):
    if p < r:
        q = partition(l, p, r)
        quicksort_rec(l, p, q - 1)
        quicksort_rec(l, q + 1, r)

# Initiate the recursion function
def quicksort(l):
    quicksort_rec(l, 0, len(l) - 1)

