l1=[("V Kohli", 100),("R Sharma", 80),("R Pant",27),("P Shaw", 34)]

a=0

for i in l1:
    a=a+i[1]
print("Total score is",a)

l2=[i[0] for i in l1 if i[1]>=50]
print(l2)