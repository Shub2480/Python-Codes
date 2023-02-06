
s="abc@#123"

d={}

d["Alphabets"]=[]
d["Digits"]=[]
d["Symbols"]=[]

for i in s:

    if i.isalpha():    
        d["Alphabets"].append(i)

    elif i.isnumeric():
        d["Digits"].append(i)
   
    else:
        d["Symbols"].append(i)
        
print(d)

