def check(a):
    return True if a%2==0 else False

a=int(input("Enter your number: "))
x=check(a)

if x:
    print("Even number")
else:
    print("Odd number")
    