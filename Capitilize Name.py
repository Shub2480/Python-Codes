s="132 456 Wq  m e"
s=s.split(" ")
print(s)
for i in range(len(s)):
    if len(s[i])==0:
        continue
    s[i]=s[i][0].upper()+s[i][1:]
s=" ".join(s)
print(s)
