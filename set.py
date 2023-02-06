a = {1,2,3,4,5}

b = {3,4,5,6,7,8,9}

c=a | b
print("Union is",c)

d=a & b
print("Intersection is ",d)

a.add(6)
print("After adding 6",a)