# In basic data structures, I said linear data structures and they are
# useful container objects. A collection of data could be searched 
# easily and they could also be found much easier if they are sorted.
# Python list have .sort() method (removed in python 3) and sorted()
# function to sort list. This builtin method could not be applied to 
# our customised linked lists or queues.
#
# I'd like to learning some comparing sort method and try to implement 
# them in python. The lower bound of comparing sort is O(NlogN) and has 
# been proved theoretically(https://en.wikipedia.org/wiki/Comparison_sort)
# (https://en.wikipedia.org/wiki/Sorting_algorithm)
# One of my friends ever told me that bogosort would be great algorithm 
# on quantum computer, I believe it's just a joke.
# Example, OrderSearch in C:
#int ordersearch(int a[], int n, int des){
#    int i;
#    for(i=0; i<n; i++)
#        if(des==a[i])
#            return 1;
#    return 0;
#}
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
# recursion version is better than that on the tutorial.
#   In C:
#binarySearch(int a[], int n, int key){
#    int low = 0;
#    int high = n - 1;
#    while(low<= high){
#        int mid = (low + high)/2;
#        int midVal = a[mid];
#        if(midVal<key)
#            low = mid + 1;
#        else if(midVal>key)
#            high = mid - 1;
#        else
#            return mid;
#    }
#    return -1;
# }
#
# Hashing:
# Python dictionary is implemented by a hash table. A hash table is 
# a table map keys to values. A python list could be seen as hash 
# table from index to its value in some degree.
# If different keys were hash to a same address, it is called 
# collision.Given a collection of items, a hash function that maps 
# each item into a unique slot is referred to as a perfect hash
# function.
# 
# Famous Hash Functions:
# 1. Folding Method: For constructing hash functions begins by
# dividing the items into equal-size pieces (the last piece may not
# be of equal size). These pieces are then added together to give
# the resulting hash value. 
#       *For example, if our item was the phone number 436-555-4601,
#       *we would take the digits and divide them into groups of 2
#       *(43,65,55,46,01). After the addition, 43+65+55+46+01, we 
#       *get 210. If we assume our hash table has 11 slots, then we
#       *need to perform the extra step of dividing by 11 and
#       *keeping the remainder. In this case 210 % 11 is 1, so the
#       *phone number 436-555-4601 hashes to slot 1. Some folding
#       *methods go one step further and reverse every other piece
#       *before the addition. For the above example, we get 43+56+
#       *55+64+01=219 which gives 219 % 11=10.
# 2. Mid-square Method:
#       *We first square the item, and then extract some portion 
#       *of the resulting digits. For example, if the item were 44,
#       *we would first compute 442=1,936. By extracting the middle
#       *two digits, 93, and performing the remainder step, we get
#       *5 (93 % 11).
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum%tablesize
# The important thing to remember is that the hash function has to be
# efficient so that it does not become the dominant part of the storage
# and search process. If the hash function is too complex, then it 
# becomes more work to compute the slot name than it would be to simply
# do a basic sequential or binary search as described earlier. This
# would quickly defeat the purpose of hashing.
#
# Collision resolution, When two keys collide, We have to deal with 
# the values collided by a systematic method.
#
# Linear Probing: Linear probing is accomplished using two values
# - one as a starting value and one as an interval between successive
# values in modular arithmetic. The second value, which is the same for
# all keys and known as the stepsize, is repeatedly added to the 
# starting value until a free space is found, or the entire table 
# is traversed. (In order to traverse the entire table the stepsize
# should be relatively prime to the arraysize, which is why the array
# size is often chosen to be a prime number.)
#   newLocation = (startingValue + stepSize) % arraySize
# Given an ordinary hash function H(x), a linear probing function
# (H(x, i)) would be:
#        H(x, i) =  (H(x) + i)(mod n), i=k% sizeoftable
# Here H(x) is the starting value, n the size of the hash table,
# and the stepsize is i in this case. Often, the step size is one;
# that is, the array cells that are probed are consecutive in the hash
# table. Double hashing is a variant of the same method in which the
# step size is itself computed by a hash function.
# This method is called rehash in online tutorial, I guess wikipedia
# gives the right definition.
# Disadvantage of linear probing is the tendency for clustering, items
# become clustered in the table. Too many values in open addresses.
#
# Alternative to linear probing, quadratic probing could be applied
# and it just change linear step to quadratic polynomial.
# My favourite method is to chaining the extra items to the same location
# in hash table as a singly liked list.
class HashTable:
    def __init__(self,size=11):
        self.size = 11              #size is arbitrary and
                                    #best to be a prime number
                                    #for efficiency
        self.slots=[None]*self.size #list * number = repeated list
        self.data=[None]*self.size
        
    def hashfunction(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size
        
    def put(self, key, data):
        hashvalue=self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data #update
            else:
                nextslot=self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
                    nextslot=self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    slef.data[nextslot]=data
                    
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                       not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):      # magical method which allows us 
                                    # get item by index of the key
        return self.get(key)

    def __setitem__(self,key,data): # magical method allows us setting
                                    # item by []
        self.put(key,data)
# Hash table could be searched or indexed in constant time O(1) while
# this would be more complex in practical since collisions.
# A well-known rule to approximate the number of comparisons necessary 
# to search for an item. The load factor, lambda, is the most important
# piece of information we need to analyze the result of a hash table.
# Conceptually, if lambda is small, then there is lower chance of 
# collisions which means the items are more likely to be in the slots
# where they belong. If λ is large, meaning that the table is filling
# up, then there are more and more collisions. This means that
# collision resolution is more difficult, requiring more comparisons
# to find an empty slot. With chaining, increased collisions means
# an increased number of items on each chain.
#
# For a successful search using open addressing with linear probing,
# the average number of comparisons is approximately 1/2*(1+1/(1−λ)) and
# an unsuccessful search gives 1/2(1+(1/(1−λ))^2) If we are using
# chaining, the average number of comparisons is 1+λ/2 for the
# successful case, and simply λ comparisons if the search is
# unsuccessful.