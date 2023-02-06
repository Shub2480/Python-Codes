s='''The lyrics are not that poor!
The lyrics are poor!'''

if "not" in s:
    if "poor" in s:
        a=s.find("not")
        b=s.find("poor")
    
        s=s.replace(s[a:b+len("poor")],"good")

print(s)