#In reading SICP, there is an amazing view that programming 
#is just abstraction(Data abstraction, procedure abstraction etc.)
#
#I have heard that CMU removed OOP course since they think it is 
#anti module and anti parallel. I guess it is because OOP based on 
#interface used to change state of object and state change is not 
#a good thing in designing programme aimed to do things parallel.
#I think immutable values is the reason why functional programming
#is useful in designing parallel and concurrency model.
#
#For me, a novice in both python and OO, OO means encapsulation, 
#information hiding and inheritance. I think it is a good way to do
#abstraction and would help me understand programming engineering
#since JAVA, an language could be written only in the way of OO, is
#so popular. 
#
#In this introduction, I'd like to introduce some basic data 
#structures.
#
#   Linear Data Structures
#       -- Stacks, queues, deque, lists
#       python list is kind of array in C (every thread online
#       said this while I am not quite sure since the element's id
#       ) but list operation do have same time complexity as array.
#       List would be seen as primitive data structure and used to
#       implement other data structures without implementing array
#       with list again
#
# I used old style or so-called classical class for typing less words.
# Old style class means super() method is not supported and 
# constructor could only be refined by referring constructor
# in base class explicitly. 
# In, multiple inheritance, method resolution order, __mro__ is a 
# little different. In old class, instead of diamond model, depth 
# first search is used.
# Also, I found that Python do not support to write instance attributes
# (self.attribute) as arguments in method. We have to set it to None,
# a tricky way.
# 
# Tips: We do not need to write constructor in python, python would 
# generate __new__ method automatically. We just need to write an
# initialise function, __init__, which would be called automatically
# when instantiating. Destructor, __del__, must be add when we 
# need it, or, the object would be dealt totally by GC.

class Stack:
    '''
        A stack is an ordered collection of items where the addition 
        of items and removal of existing items take place at the same
        end. It is a Last-In, First-Out(LIFO) structure.
    '''
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
        
    def push(self, item):
        # considering about list is an array, append takes constant time
        # and insert at the beginning takes linear time. 
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def getTop(self):
        if len(self(items))==0:
            raise Exception('empty,stack')
        return self.items[-1]
        
    def size(self):
        return len(self.items)
  
    def Clear(self):
        del self.items[:]
    # Stack is a general model of memory and frequently used in 
    # balancing symbols(by maintaining a stack to be empty).
    # Also, it could be used to tracking errors as used in python 
    # or tracking the 0s & 1s used to convert decimal to binary(
    # recursion problems to be exactly).
    # Stack is very important in parsing techniques.
        
#########################################################

class Queue:
    '''
        A queue is analogy to the queue in relativity.
        In contrast to stack, it is FIFO(first in first out) structure
        It could be seen as subclass as Queue even though I write it as 
        a base class.
    '''
    def __init__(self):
        self.items=[]
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
    # This method takes linear time as pop happened at the beginning
    # of an array.
    # Implementation by linked list might improve efficiency.
        return self.items.pop(0)
        
    def isEmpty(self):
        return self.items==[]
        
    def size(self):
        return len(self.items)
    # As a basic data structure, queue is used extensively in simulating
    # data waited to be managed or tasks to be executed.
    
        
#########################################################

class Deque:
    '''
        A deque, know as double-ended queue, is a queue which could be 
        operate on both ends.
    '''
    def __init__(self):
        self.items=[]
     
    def addFont(self, item):
        self.items.insert(0,item)
        
    def addRear(self,item):
        self.items.append(item)
        
    def removeFont(self):
        return self.item.pop(0)
        
    def removeRear(self):
        return self.item.pop()
        
    def isEmpty(self):
        return self.items==[]
        
    def size(self):
        return len(self.itmes)
        
###########################################################

class Node:
    '''
        Node is the basic building block for implementing a linked list
        The node must hold at least the item stored in this node and 
        the reference to next node, like pointer in C.
    '''
    def __init__(self, initData):
        self.__data=initData
        self.__next=None
    
    def getData(self):
        return self.__data
        
    def getNext(self):
        return self.__next
        
    def setData(self, newData):
        self.__data=newData
        
    def setNext(self, newNext):
        self.__next=newNext
    
    # def __del__(self):
        # pass
    # This is the destructor in Python(constructor is __new__, not 
    # __init__). I do not use it since python have automate garbage 
    # collection. Honestly speaking, __del__ is not called every
    # time when we del sth in some reasons I do not know yet and 
    # I do not want to activate gc.collection() manually.
    # Attention: __del__ would disturb GC if we have write sth
    # circular referenced.
        
class singlyCyclelList:
    '''
        As the name, singlyCyclelList is a singly linked list and also
        a cycle list. I just give a singly cycled list since I believed 
        it is the easiest version of linked list. Isn't it?
    '''
    def __init__(self, item=None):
        self.head=Node(item)
        self.head.setNext(self.head)
        
    def add(self, item):
        temp=Node(item):
        temp.setNext(self.head.getNext())
        self.setNext(temp)
        
    def isEmpty(self):
        if self.head.getNext() is self.head \
            and self.head.getData()==None:
            return True
        else:
            return False
        # I hope this work, but I think it would fail if we set
        # the data in head to None. I am confused and I hope I 
        # would figure it out latter since I would like to read 
        # books on data structures, uh, after exam.
        
    def search(self,item):
        current=self.head
        while current.getData() != item:
            if current.getNext() is self.head:
                raise Exception('item not in list
            else:
                current=current.getNext()
            return True
        
    def remove(self, item):
        current=self.head
        prev=None
        while current.getData() != item:
            prev=current
            current=current.getNext()
            if current is self.head:    # is means same object
                raise Exception('item is not in the list')
        else:
            prev.setNext(current.getNext())
            # The Node which is just removed is still there with no 
            # reference and would be deleted when GC is activated.

# Tips:
#       1. List is Array in C despite the id of elements are not 
#          continuous. Elements in list are just pointers to objects.
#          OK, I am trying to figure out how to write
#          C Pythonicly.
#           typedef struct              {
#               PyObject_VAR_HEAD
#               PyObject **ob_item      ;
#               Py_ssize_t allocated;
#                                       }
#               PyListObject            ;
#       2. Dict in python is implemented by hash table and all the 
#          operations except sth like iteration all takes constant
#          time.
#
#
# References: 1. introduction to algorithms.
#             2. Wikipedia (I do not want to say it, but I did not 
#                have time to read books in library and so I used 
#                wikipedia as cheat sheet)