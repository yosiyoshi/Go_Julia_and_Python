"""
Author: Yosiyoshi
"""
h=[2,3,4,5]
function calc(array)
           x=[0,0,0,0]
           for n in 1:length(array)
               x[n]=array[n]^2
           return x,n
           end
       end
calc(h)
