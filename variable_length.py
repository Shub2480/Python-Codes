def fact(*n):
    for i in n:
        a=1
        for j in range(1,i+1):
            a=a*j

        print(a)


fact(4,5,6,7,8)

print("\n")


def display(**n):
    x=n.keys()
    a=n.values()
    print(x)
    print(a)
display(rno=100,name="Shubham",marks=70,subject="Python")