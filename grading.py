marks=int(input("Enter your marks:"))

if marks>=80:
    grade="A+"

elif marks>=70:
    grade="A"

elif marks>=60:
    grade="B"

elif marks>=50:
    grade="C"

elif marks>=40:
    grade="D"

elif marks<40:
    grade="FAIL"

else:
    print("Wrong input")

if grade=="FAIL":
    print("You are fail")
else:
    print("You have got grade",grade)