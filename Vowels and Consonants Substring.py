s="BANANA"

v=["A","E","I","O","U"]
stuartl=[]
kevinl=[]
for i in range(len(s)):
    if s[i] in v:
        for j in range(i,len(s)+1):
            string=s[i:j]
            if  len(string)!=0:
                kevinl.append(string)
kevin=len(kevinl)
print(kevin)




for i in range(len(s)):
    if s[i] not in v:
        for j in range(i,len(s)+1):
            string=s[i:j]
            if  len(string)!=0:
                stuartl.append(string)
stuart=len(stuartl)
print(stuart)
    
