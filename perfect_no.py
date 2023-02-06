def perfect(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a=a+i
    
    if a==n:
        return "Perfect number"
    else:
        return "Not a perfect number"

a=int(input("Enter number:"))
print(perfect(a))
