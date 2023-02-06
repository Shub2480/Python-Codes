num=int(input("Enter year:"))

if num%400==0:
    print(num,"is leap year")
    
elif num % 4 ==0: 
    if num % 100 != 0:
        print(num,"is leap year")
    else:
        print(num,"is not a leap year")

else:
    print(num,"is not a leap year")
