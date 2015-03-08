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
#       said this while i am not quite sure since the element's id
#       ) and would be seen
#       as primitive data structure and used to implement other
#       data structures without implementing array with list again
#
# I used old style or so-called classical class for typing less words.
# Old style class means super() method is not supported and 
# constructor could only be refined by referring constructor
# in base class explicitly. 
# In, multiple inheritance, method resolution order, __mro__ is a 
# little different. In old class, instead of diamond model, depth 
# first searching is used.
# Also, I found that Python do not support to write instance attributes
# (self.attribute) as arguments in method. We have to set it to None,
# a tricky way.

class Stack:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def getTop(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)
  
    def Clear(self):
        del self.items[:]
        
#########################################################

class Queue:
    def __init__(self):
        self.items=[]
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
        
    def isEmpty(self):
        return self.items==[]
        
    def size(self):
        return len(self.items)
        
#########################################################

class Deque:
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
        
class singlyCyclelList:
    def __init__(self):
        self.head=Node(None)
        self.head.setNext(self.head)
        
    def add(self, item):
        temp=Node(item):
        temp.setNext(self.head.getNext())
        self.setNext(temp)
        
    def remove(self, item):
        current=self.head
        prev=None
        while current != item:
            prev=current
            current=current.getNext()
            if current is self.head:    # is means same object
                raise Exception('item is not in the list')
        else:
            prev.setNext(current.getNext())
            
        
        


        
        
        
        
        
        
        
        
        