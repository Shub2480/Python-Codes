
lists = [[1,4,5],[1,3,4],[2,6]]

listt=[]

for i in lists:
    for j in i:
        listt.append(j)

a=sorted(listt)
print(a)
