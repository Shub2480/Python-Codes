nums = [0,0,1,1,1,2,2,3,3,4,5,5]


newnum=[]

for i in nums:
    if i not in newnum:
        newnum.append(i)
print(newnum)
