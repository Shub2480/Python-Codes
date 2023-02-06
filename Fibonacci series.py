'''s=1
i=0

while s<100:
    print(s)
    i=i+s
    s=s+i 
    print(i)
    
'''
'''
a=0
def sumrecrr(n):
    if n==1:
        return 1
    else:
        return n + fib(n-1)   
print(fib(5))

'''
'''
def fib(n):
    
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)
        
print(fib(6))
'''


