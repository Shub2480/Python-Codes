num=int(input("Enter number"))
rev=0

while num>0:
    a=num%10
    rev=(rev*10)+a
    num=num//10
print(rev)
