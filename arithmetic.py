a,b=[int(x) for x in input("Enter 2 numbers    ").split()]
c=input("Enter operator    ")
if c=="+":
    print("a+b=",a+b)
elif c=="-":
    print("a-b=",a-b)

elif c=="*":
    print("a*b=",a*b)
elif c=="/":
    print("a/b=",a/b)
else:
    print("Wrong input")

