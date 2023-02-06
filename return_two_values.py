def calculation(a,b):
    return a+b,a-b

a,b=[int(x) for x in input("Enter two numbers").split()]
x,y=calculation(a,b)

print("Addition and Subtraction of number is:",x,"and",y)


