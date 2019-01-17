# coding: utf-8
# Your code here!
# Author: Yosiyoshi
import random
def arith(a,b):
    return a+b, a-b, a*b, a/b
def bmi(w,h):
    result=w/h**2
    if result<18.5:
        return "slender"
    elif 18.5<=result<25:
        return "intermediate"
    elif 25<=result<30:
        return "fat"
    elif 30<=result:
        return "stout"
def cash(a):
    return [a//10000, a%10000//5000, a%5000//1000, a%1000//500, a%500//100, a%100//50, a%50//10, a%10//5, a%5]
def rsp(a):
    comp=random.randint(0,2)
    while 0<=a<=2:
        if comp<a:
            return "You won!"
        if comp==a:
            return "Draw!"
        if comp>a:
            return "You lose!"
    else:
        return "Invalid."
def bargraph(length):
    graph=u""
    for i in range(0, length):
        graph=graph+u"■"
    return graph
# sample codes
print(arith(5,2))
print(bmi(50,1.7))
print(cash(48767))
print(rsp(1))
print(bargraph(3))

