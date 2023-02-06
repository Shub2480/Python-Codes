x = [2,4,6,8,10]

x.append("eleven")
print(x)

x.insert(0,"one")
print(x)

y= [12,13,14]
print(x)

x=x+y
print(x)

x.reverse()
print(x)

for i in range(3,6):
    x.pop(i)
print(x)

x.remove("one")
print(x)

x = ["hey","there","hello","world"]
y=" ".join(x)
print(y)