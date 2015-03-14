################################
# Sorting
################################
# A sorting algorithm is an algorithm that puts elements of a list
# in a certain order. The most-used orders are numerical order and
# lexicographical order. Efficient sorting is important for optimizing
# the use of other algorithms (such as search and merge algorithms
# which require input data to be in sorted lists; it is also often
# useful for canonicalizing data and for producing human-readable
# output. More formally, the output must satisfy two conditions:
#       1. The output is in nondecreasing order (each element is no
#          smaller than the previous element according to the desired
#          total order);
#       2. The output is a permutation (reordering) of the input.
# The time complexity and comparison of sorting algorithm could be 
# read on wikipedia(https://en.wikipedia.org/wiki/Sorting_algorithm)
#
####################
# Famous bubble sort
# The bubble sort makes multiple passes through a list. It compares
# adjacent items and exchanges those that are out of order. Each pass
# through the list places the next largest value in its proper place.
# In essence, each item “bubbles” up to the location where it belongs.
def bubbleSort(alist):
    for num in range(len(alist)-1,0,-1):
        for i in rang(num):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]