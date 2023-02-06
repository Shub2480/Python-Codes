s=4

for i in range(2,s):
    if s%i==0:
        print("Not Prime")
        break
else:
    print("Prime")


a=100

for i in range(2,a):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
