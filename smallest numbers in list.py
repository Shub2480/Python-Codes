l=[14,6,5,13,9,8,7,11,12,4]

min=l[0]
max=l[0]
sum=0

for i in range(len(l)):
    if l[i]<min:
        min=l[i]
    if l[i]>max:
        max=l[i]
    sum=sum+l[i]
    
print("Sum of all number is",sum)
print("Smallest number is",min)
print("Largest number is",max)
