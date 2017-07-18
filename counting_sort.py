####################################################
#                counting sort                     #
####################################################
# Assuming that all the numbers in the array       #
# are between 0 and k, we can use counting sort    #
#                                                  #
# In counting sort, we use one array for store     #
# data which has the length of k and a array       #
# for storing final result.                        #
#                                                  #
# The performance of counting sort is O(n)         #
#                                                  #
####################################################


def counting_sort(s, k):
    result, temp = [0]*len(s), [0]*k
    for item in s:
        temp[item] = temp[item] + 1
    for i in range(k):
        if i > 0:
            temp[i] = temp[i] + temp[i - 1]

    for j in range(len(s)-1, -1, -1):
        result[temp[s[j]] - 1] = s[j]
        temp[s[j]] = temp[s[j]] - 1

    return result



