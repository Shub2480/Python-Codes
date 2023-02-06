num = int(input("Enter a number:"))

temp=num
rev=0
while temp>0:
    pal=temp%10
    rev=(rev*10)+pal
    temp//=10

if num==rev:
    print(num,"Number is palindrome")
else:
    print(num,"Number is not palindrome")
