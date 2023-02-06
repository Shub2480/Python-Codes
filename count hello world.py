s="hello world"

d={}

for i in s:
    if i in d :
        continue
    elif i==" ":
        continue
    else:
        d[i]=s.count(i)

print(d)