#########################
# Recursion:
#########################

# In mathematics and computer science, a class of objects or methods
# exhibit recursive behavior when they can be defined by two 
# properties:
#    1. A simple base case (or cases)
#    2. A set of rules that reduce all other cases toward the base case
#
# For example, calculate the sum of a list.
#
# of course we could iterate the list by for statement or just
# call reduce(lambda: x,y:x+y, list)
# but we could also do it by recursion:
def summ(list):
    if len(list)==1:
        return list[0]
    else:
        return list[0] + summ(list[1:])
# This kind of recursion by calling itself in the end is called 
# Tail recursion.
# I heard that some functional programming language like Haskell would optimise
# tail recursion to iterative method. But python do not support this 
# feature and Guido van Rossum have explained long time ago:
# http://neopythonic.blogspot.com.au/2009/04/tail-recursion-elimination.html
# http://neopythonic.blogspot.com.au/2009/04/final-words-on-tail-calls.html
#
# The classical recursive problem is hanoi tower. I assume everyone
# know that game and the code to solve hanoi tower is recursive and 
# we also use leap of faith to assume we know how to solve complex
# hanoi problems.
#
def hanoi(height, beginning='begin pole', end='end pole'\
           , help='help pole'):
    if height <= 0:
        raise Exception('wrong height, at least 1')
    elif height == 1:
        return moveDisk(beginning, end)
    else:
        hanoi(height-1, beginning, help, end) # we assume we know how 
                                              # to move height-1 disks
        moveDisk(beginning, end)
        hanoi(height-1, help, end, beginning)
        
def moveDisk(position1, position2):
    print 'move disk from %s to %s' %(position1, position2)

# If I do not remember the wrong, I believe, SICP(Structure and 
# Interpretation of Computer Programs) gave an example on 
# changing money.
#
# It is about change 100 pence(1 Pound) money to 50 pence, 20 pence,
# 10 pence, 5 pence, 2 pence and 1 penny coins. How many ways do we 
# have ?
ListOfCoins=[1,2, 5, 10, 20, 50]
def ChangeMoney(amount=100, coin=ListOfCoins):
    if amount == 0:
        return 1        # only 1 method if the amount is 0
    elif amount <= 0 or len(coin) == 0:   
        return  0       # no way to change negative amount of money
                        # or with no coin
    else:
        return ChangeMoney(amount,coin[1:]) + ChangeMoney(amount-coin[0])
        # change the money without largest value coin plus with 
        # the largest coin.

# It is obviously that recursion method is really easy for solving 
# very complex problems. And it is not hard to find that the method
# used to calculate total ways of changing money is quite slow.
#
# The disadvantages of recursion method is that it takes longer time 
# and memory to call functions recursively.
# There are many tutorials online demonstrated how to change tail 
# recursion to iteration if the logic in the recursive version is 
# too complex to rewrite(such as this example...).

#########################
# Divide and conquer
#########################
pass
# I do not have examples in my mind yet. Wikipedia does not 
# give any example neither TAT, bad luck.


#########################
# Monty carlo
#########################
# I guess this would be the most important part in computational 
# physics which is and optional class I would like to choose next
# next year. Yo, I am not just wasting my time.

# According to wikipedia:
# Monte Carlo methods (or Monte Carlo experiments) are a broad
# class of computational algorithms that rely on repeated random 
# sampling to obtain numerical results. They are often used in 
# physical and mathematical problems and are most useful when it is
# difficult or impossible to use other mathematical methods. Monte
# Carlo methods are mainly used in three distinct problem classes:
# optimization, numerical integration, and generation of draws from
# a probability distribution.
#
import random
f=random.random
def MCforPI(n):#find PI by Monty carlo method
    X=[f() for i in xrange(n)]
    Y=[f() for i in xrange(n)]
    points=zip(X,Y)             #generate point in region [0,1)
    circle=filter(lambda (x,y): x**2+y**2<=1,points)#find points in quarter
                                                    #circle with radius 1
    # to make this block more efficiency, list could be replaced 
    # by generator, a small optimization method.
    PI='%.10f' % (1.*len(circle)/len(points)/0.25)
    return PI
    
#######################################
# Greedy method & Dynamic Programming
#######################################
#
#