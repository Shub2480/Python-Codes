l=[2,3,4,55,56,78,75,69,66,101,100]

e=0
o=0

for i in l:
    if i%2==0:
        e=e+1
    else:
        o=o+1

print("The total number of even numbers are",e)
print("The total number of odd numbers are",o)
