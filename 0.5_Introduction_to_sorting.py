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
######################################
# Famous bubble sort & selection sort
#
# The bubble sort makes multiple passes through a list. It compares
# adjacent items and exchanges those that are out of order. Each pass
# through the list places the next largest value in its proper place.
# In essence, each item “bubbles” up to the location where it belongs.
def bubbleSort(alist):
    for num in range(len(alist)-1,0,-1):
        for i in rang(num):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
# bubble sort has worst case and average complexity O(n^2) and is
# often considered the most inefficient sorting method.
#
# The selection sort improves on the bubble sort by making only one
# exchange for every pass through the list. In order to do this, a
# selection sort looks for the largest value as it makes a pass and,
# after completing the pass, places it in the proper location. As
# with a bubble sort, after the first pass, the largest item is in
# the correct place. After the second pass, the next largest is in
# place. This process continues and requires n−1 passes to sort n
# items, since the final item must be in place after the (n−1) st
# pass.
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
# Selection sort makes the same number of comparisons as the bubble
# sort and is therefore also O(n^2). Due to the reduction in the number
# of exchanges, the selection sort typically executes faster in
# benchmark studies.
#