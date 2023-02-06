n=8

for i in range(n):
    print(" "*(n-i),end="*")
    if i==n-1:
        print("*"*((i*2)-1),end="*")
    if i>0 and i<n-1 :
        print(" "*((i*2)-1),end="*")
    
    print()

 


for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    if i>1:
         for k in range(i-1,0,-1):
             print(k,end="")
    print()
