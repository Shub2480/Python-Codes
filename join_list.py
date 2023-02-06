x= [1,2,3]
y=['a','b','c']

new=[(x[a],y[b]) for a in range(len(x)) for b in range(len(y))]

print(new)