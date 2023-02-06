def neon(n):
    temp=n*n
    no=0
    while temp>0:
        a=temp%10
        no=no+a
        temp//=10
    if no==n:
        return "Neon Number"
    else:
        return "Not a neon number"

n=int(input("Enter number: "))
print(neon(n))