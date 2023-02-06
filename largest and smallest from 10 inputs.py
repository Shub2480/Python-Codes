large=int(input("Enter first number"))
small=large
for i in range(10):

    num=int(input("Enter next numbers"))
    
    if num>large:
        large=num
    
    if num<small:
        small=num

print("Largest number is",large)
print("Smallest number is",small)