n=4

for i in range(1,n):
    print("-"*(i*3),end="")
    for j in range(1):
        print("*"*(n*n-i*i))
