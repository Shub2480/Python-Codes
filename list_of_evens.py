def evens(s,e):
    l=[x for x in range(s,e+1) if x%2==0]
    return l

a=int(input("Enter start point:"))
b=int(input("Enter end point:"))

print(evens(a,b))