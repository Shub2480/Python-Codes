nums=[2,2,3,4,4,3,3]
val=5

if val in nums:
    a=nums.count(val)
    for i in range(a):
       nums.remove(val)
    print(nums)
else:
    print(f"No {val} found in the list")
