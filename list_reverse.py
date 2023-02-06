myList = [10,"abc",20,3.5,"xyz"]

newList=[]
for i in range(1,len(myList)+1):
    newList.append(myList[-i])

print(newList)
