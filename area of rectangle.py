len=float(input("Enter length:"))
brd=float(input("Enter breadth:"))

area=(len*brd)

if len==brd:
    print("It is a square")
    print("Area of this square is",area)

else:
    print("Area of this rectangle is",area)
