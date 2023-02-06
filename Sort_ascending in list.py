l1=[]
a=[2,3,4,5,1]    
for i in range(len(a)):
    min=a[0]
    for x in a:
        if x<min:
            min=x
      
    a.remove(min)
    l1.append(min)

print(a,l1)