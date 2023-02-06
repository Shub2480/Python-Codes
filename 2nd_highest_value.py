a=[2,3,8,4,5,1,7,6,8,4]
a=list(set(a))
b=[]

while a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
        
    a.remove(min)
    b.append(min)

print("Second highest value is",b[-2])