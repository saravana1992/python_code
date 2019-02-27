# following lines to take three numbers from user
x=int(input("enter the number of x:"))
y=int(input("enter the number of y:"))
z=int(input("enter the number of z1:"))
if x > y:
    if x > z:
        print("number x is greatest:", x)
    else:
        print("number z is greatest:", z)
elif y > z:
    if y > x:
        print("number y is greatest:", y)
    else:
        print("number z is greatest:", z)
elif z > x:
    if z > y:
        print("number z is greatest:", z)
    else:
        print("number y is greatest:", y)