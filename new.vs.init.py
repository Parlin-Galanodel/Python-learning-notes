# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:43:26 2016

@author: Galanodel
"""

# No actual __new__ method in old style class:
class A:
    def __new__(cls):
        print "A.__new__ is called"  # -> this is never called

A()


# __init__ make sense:
class B:
    def __init__(self):
        print "B.__init__ called"

B()


# __init__ methods should return None:
class C:
    def __init__(self):
        return 29

#C()


# the order of __new__ and __init__:
class D(object): 
    def __new__(cls):
        print "D.__new__ called"
        return super(D, cls).__new__(cls)

    def __init__(self):
        print "D.__init__ called"

D()