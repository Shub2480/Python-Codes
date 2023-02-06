x= [1,2,3]
y=['a','b','c','d']


new=[]

for i in range(len(x)):
    for j in range(len(y)):
        new.append((x[i],y[j]))
print(new)

