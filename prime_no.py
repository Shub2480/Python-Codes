def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")

n=int(input("Enter number: "))
prime(n)