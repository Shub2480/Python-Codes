list1=[]

for i in range(1900,2031):
    if i%400==0:
        list1.append(i)
    elif i%4==0:
        if i%100!=0:
            list1.append(i)

print(list1)

