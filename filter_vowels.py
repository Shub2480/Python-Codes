string="Hello World From IT Vedant"

l=list(filter(lambda x: x.lower() in ["a","e","i","o","u"] , string))
print(l)