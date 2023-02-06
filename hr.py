s=['T%Mic&', 'h%axr%', 'iit#p!', 'ssrst&']

'''

00
10
20
30


'''
m=6
n=4
l=[] 
for i in range(m):
    for j in range(n):
        l.append(s[j][i])
l="".join(l)
k=l
# This$#is% Matrix#  %!
b=""
flag=False
for i in l:
    if i.isalnum():
        if flag==True:
            b=str(b)+" "
            flag=False
        b=str(b)+i
    else:
        flag=True
mix=len(k)-(k[::-1].find(b[-1]))
b=str(b)+k[mix:]
print(b)

