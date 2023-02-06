nums = [-1,0,1,2,-1,-4]

l=[]
for i in range(len(nums)):
    
    for j in range(i+1,len(nums)):
        inner=[]
        f2=nums[i]+nums[j]
        print(nums[i])
        print(nums[j])
        t=0-f2
        print(t)
        if t in nums[j+1:]:
            print("Yes")
            inner.append(nums[i])
            inner.append(nums[j])
            inner.append(t)
            l.append(inner)

print(l)
