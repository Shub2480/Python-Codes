s = 'AABCAAADAkljgyisssnu'
k = 5

br=len(s)/k
l=[]
for i in range(int(br)):
    print(i)
    sts=s[:k]
    s=s[k:]
    l.append(sts)
print(l)

fl=[]
for i in l:
    nl=[]
    for j in i:
        if j not in nl:
            nl.append(j)
    fl.append(nl)

for i in range(len(fl)):
    for j in range(len(fl[i])):
        print(fl[i][j],end="")
    print("")
    
