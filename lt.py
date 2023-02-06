s="1.234"

s=s.lstrip().rstrip()

s=s.split(" ")

n=0
for i in s:
    
    if i.isalpha():
       
        break
    elif len(i)==0:
       
        continue
    else:
        
        
        n=i
        break

if "." in n:
    print(int(float(n)))
    
if int(n)<0 and len(n)>10:
    print( -2**31)
elif int(n)>0 and len(n)>9:
    print ((2**31)-1)
else:
    print( int(n))
