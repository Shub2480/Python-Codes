n=[0,1,1,1,0,0,1,1]

c=0

for i in range(len(n)):
    
    if n[i] == 0:
        a=n[i:].count(1)       
        c=c+a
        
print(c)
