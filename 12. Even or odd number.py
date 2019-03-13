def eoo(x):
    even = 0
    odd = 0

    for i in x:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


lst=(1,22,33,44)

evenorodd= eoo(lst)

print(even)
