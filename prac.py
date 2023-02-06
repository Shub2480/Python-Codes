N = int(input())
    
l=[]
    
for i in range(N):
    a,b=input("op:"),input("i").split()
    cmd=str(a)    
    if a=="print":
        print(l)
    else:
        eval("l."+cmd+"("+",".join(b)+")")
