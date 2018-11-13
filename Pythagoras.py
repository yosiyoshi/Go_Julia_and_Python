# -*- coding: utf-8 -*-

"""
Author: Yosiyoshi
"""
import math

def pythag(a,b):
    c2=a**2+b**2
    c=math.sqrt(c2)
    return c
    
def pythag2(a,b):
    if a>=b:
        c2=a**2-b**2
        c=math.sqrt(c2)
        return c
    if a<b:
        c2=b**2-a**2
        c=math.sqrt(c2)
        return c

print(pythag(3,4))
print(pythag(math.sqrt(2),math.sqrt(2)))
print(pythag2(5,4))
print(pythag2(4,5))