# In basic data structures, I said linear data structures and they are
# useful container objects. A collection of data could be searched 
# easily and they could also be found much easier if they are sorted.
# Python list have .sort() method (removed in python 3) and sorted()
# function to sort list. This builtin method could not be applied to 
# our customised linked lists or queues.
#
# I'd like to learning some comparing sort method and try to implement 
# them in python. The lower bound of comparing sort is NlogN and has 
# been proved theoretically(https://en.wikipedia.org/wiki/Comparison_sort)
# (https://en.wikipedia.org/wiki/Sorting_algorithm)
# One of my friends ever told me that bogosort would be great algorithm 
# on quantum computer, I believe it's just a joke.
#
# Sorting should be applied first to a sequence if we want to use special
# search method like binary search. But I would use the order in 
# Problem Solving with Algorithms and Data Structures,
# (http://interactivepython.org/runestone/static/pythonds/index.html)
# it is a good and concise introduction to algorithm and data structures
# free online and it's in python.
# I would not go back to review other contents before sorting and 
# searching in that guide but I guess I would read it if necessary.
#
def binarySearch(alist, item):
    first=0
    last=len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    return found
# Online tutorial said this is also divide & conquer method, I am not 
# quite happy with this conclusion, I'd like to find some problems
# which could be solved by dividing to many independent functions.
#
# I am learning algorithm, so I will implement it on my own again as
# I did in other part of the notes before I found this tutorial.
def myBinarySearch(alist, item):
    L=len(alist)//2
    if len(alist)==0:
        return False
    elif alist[L]==item:
        return True
    elif alist[L]>item:
        return myBinarySearch(alist[:L],item)
    elif alist[L]<item:
        return myBinarySearch(alist[L+1:],item)
# I do it by recursion and as mentioned before, iteration method is 
# much better as less variable to track at the same time. But 
# recursion version is really easy to be understood. I think my
# recursion version is better than it on the tutorial.
#
# Hashing:
# Python dictionary is implemented by a hash table. A hash table is 
# a table map keys to values(which the memory addresses by a hash
# function). A python list could be seen as hash table from index
# to its value(despite they are an array of pointers, but we do 
# calculate the memory address of an element when visiting it) in
# some degree.
#

