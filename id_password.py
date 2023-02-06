def login(id,pw):
    dict={"Shubham":1234,
"Mangesh":2345,
"Akshay":3456,
"Saksham":4567,
"Yash":5678,
"Sarfaraz":6789,
"Sameer":7890}
    

    if id in dict:
        if dict[id]==pw:
            print("\nLoggedin")
                
                
        else:
            print("\nWrong user Id or password")
            a=input("Enter your id again:")
            b=int(input("Enter your password"))
            login(a,b)
    else:
        print("\nNo id exist...")
        a=input("Enter your id again:")
        b=int(input("Enter your password"))
        login(a,b)

id=input("Enter your Id:")
pw=int(input("Enter your password:"))
login(id,pw)