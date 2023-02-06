a=float(input("Enter side one of triangle:"))
b=float(input("Enter side two of triangle:"))
c=float(input("Enter side three of triangle:"))

if a==b and b==c:
    print("Its a equilateral traingle")
elif a!=b and b!=c and c!=a:
    print("Its a Scalene triangle")
elif a==b or b==c or c==a:
    print("Its a Isoscales triangle")
