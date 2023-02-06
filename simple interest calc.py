gender=input("Enter your gender M/F:")
age=int(input("Enter your age:"))
fda=int(input("Enter your fixed deposit amount:"))

if gender=="f" and age>=60:
    interest="8%"
    total=fda*1.08

elif gender=="f" and age<60:
    interest="7%"
    total=fda*1.06

elif gender=="m" and age>=60:
    interest="6%"
    total=fda*1.07

elif gender=="m" and age<60:
    interest="5%"
    total=fda*1.05

else:
    print("wrong input")


print("your total amount after",interest,"is",total)