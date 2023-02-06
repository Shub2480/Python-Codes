num=int(input("Enter a number"))

sum=0
temp=num
while temp>0:
    a=temp%10
    sum=sum+(a**3)
    temp=temp//10
    

if sum==num:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")