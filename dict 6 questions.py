d = {'a':10,'b':30,'c':50,'d':100}

d["b"]=300
print(d)

if "e" in d:
    print(d["e"])
else:
    print("e does not exist")

d["e"]=600
print(d)

print(d.values())

x = {'i':11,'j':12,'k':13,'l':14}

d.update(x)
print(d)

print(d.pop("j"))
print(d)