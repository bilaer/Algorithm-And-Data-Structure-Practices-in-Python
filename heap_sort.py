####################################
#           Heap Sort              #
# ##################################
#                                  #
# Max_heapify: O(lgn)              #
# Build_max_heap: O(n)             #
# Overall performance is O(nlgn)   #
#                                  #
####################################
import math

# Calculate the index of left child of certain root
def get_left_child(l, index):
    if index == 0:
        return 1
    else:
        return 2*index + 1

# Calculate the index of right child of certain root
def get_right_child(l, index):
    if index == 0:
        return 2
    else:
        return 2*(index + 1)

# Exchange the values in two places of a given list
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

# Change a heap into the max heap
def max_heapify(l, index, heap_size, depth=0):
    indent = "  "*depth
    left = get_left_child(l, index)
    right = get_right_child(l, index)
    largest = index
    if left < heap_size and l[left] > l[largest]:
        largest = left

    if right < heap_size and l[right] > l[largest]:
        largest = right

    # If root don't have largest values, change the value with
    # it's child which has the largest value and do the recursion
    if largest != index:
        swap(l, index, largest)
        print(indent + "the index of largest: %d\n" %(largest))
        max_heapify(l, largest, heap_size, depth+1)
    else:
        return

def build_max_heap(l):
    heap_size = len(l)
    for index in range(math.ceil(len(l)/2), -1, -1):
        print("the index: %d\n" %(index))
        max_heapify(l, index, heap_size)

def heap_sort(l):
    # Exchange the value at the end of the list to the font and build the list again
    build_max_heap(l)
    heap_size = len(l)
    for i in range(len(l)-1, 0, -1):
        swap(l, i, 0)
        heap_size = heap_size - 1
        max_heapify(l, 0, heap_size)

