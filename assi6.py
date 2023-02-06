string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"

a=""
for i in range(0,len(string)):
    if i%4==0 and i!=0:
        a=a+"\n"
    
    a=str(a+string[i])


print(a)