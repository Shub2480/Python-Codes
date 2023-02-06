s="MDCXCV"
d={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,

}

last=True
nxt=False
a=0

for i in range(len(s)-1):
    last=False

    if nxt == True:
        nxt=False
        if i == len(s)-2:
            last=True
        continue     
    elif d[s[i]] < d[s[i+1]]:
        a=a+(d[s[i+1]]-d[s[i]])
        nxt=True
        
        
    else:

        a=a+d[s[i]]
        
        last=True
    
if last==True:
    
    a=a+d[s[-1]]

print(a)
