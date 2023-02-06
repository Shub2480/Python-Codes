x=511232115


x=str(x)


if x == x[::-1]:
    print( "true")
else:
    print( "false")
c=0

for i in range(1,len(x)+1):
    c=10*c+(int(x[-i]))
if str(c)==x:
    print( "true")
else:
    print( "false")    
    
