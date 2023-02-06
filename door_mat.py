n,m=[int(x) for x in input().split()]

for i in range(1,int(((n-1)/2)+1)):
    
    print("-"*int((((((m-1)/2)-1)-i*3)+3)),end="")
    for j in range(1):
        print(".|."*((i*2)-1),end="")
        for k in range(1):
            print("-"*int((((((m-1)/2)-1)-i*3)+3)))

print("-"*int((m-7)/2)+"WELCOME"+"-"*int((m-7)/2))

for i in range(1,int(((n-1)/2)+1)):
    print("-"*(i*3),end="")
    for j in range(1):
        print(".|."*int(n-i-i),end="")
        for k in range(1):
            print("-"*(3*i))