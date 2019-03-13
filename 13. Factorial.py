

def fact(x):

    f=1

    for i in range(1,x+1):

        f=f*i

    return f

x=int(input("enter value to fact: "))

y=fact(x)

print(y)