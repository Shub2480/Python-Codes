rs=float(input("Enter Amount: "))
yrs=float(input("Enter duration in years: "))
ints=float(input("Enter expected interest rate: "))
rs=rs*12
intss=1+(ints/100)

def rec(rs,yrs,intss):
    if yrs<1:
        return 0
    a=rs*intss
    return a + rec(a,yrs-1,intss)

print(rec(rs,yrs,intss))
