n="HACK"
m=2
from itertools import permutations

l=list(permutations(n,int(m)))

for i in range(len(l)):
    
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
    print("")

