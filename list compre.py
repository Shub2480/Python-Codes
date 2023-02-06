l=[]
k=[]


for _ in range(int(input("number"))):
    name = input("name")
    score = float(input("marks"))
    l.append([name,score])
       
    
s=sorted(list(set(i[1] for i in l)))[1]

print(s)
    
for i in l:
    if s==i[1]:
        k.append(i)
        print(k)
            
for i in sorted(k):
    print(i[0])
    print(i)    