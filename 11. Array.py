
from array import *

arr=array('i',[])

n=int(input("enter the length of string:  "))

print(n)

for i in range(n):
    x=int(input("enter the value: "))
    arr.append(x)

print(arr)

k=0

y=int(input("enter the number: "))

for e in arr:
    if e==y:
        print(k)
        break

    k+=1