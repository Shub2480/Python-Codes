n=7

for i in range(n):
    print(" "*i,end="")
    for j in range(65,65+n-i):
        print(chr(j),end="")
    print()


for i in range(n):
    print(" "*i,end="")
    for j in range(65+i,65+n):
        print(chr(j),end="")
    print()




for i in range(n):
    #print(" "*i,end="")
    for j in range(65+i,65+n):
        print(chr(j),end="")
    print()


for i in range(n):
    #print(" "*i,end="")
    for j in range(65,65+n-i):
        print(chr(j),end="")
    print()

for i in range(n):
    for j in range(0,i+1):
        print(chr(65+j),end="")
    print()
    
