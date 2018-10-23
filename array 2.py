h=[2,3,4,5]
def calc(array):
    x=[0,0,0,0]
    for n in range(0,len(array)):
        x[n]=array[n]**2
    return x,n

print(calc(h))
