def sort1(a):
    l1=[]    
    while a:
        min=a[0]
        for x in a:
            if x>min:
                min=x
        
        a.remove(min)
        l1.append(min)
    
    return l1

x=[2,3,4,5,1]
print(sort1(x))