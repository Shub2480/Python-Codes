
l=['abc', 'xyz', 'aba', '1221','343','def']

count=0

for i in l:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1

print(count)