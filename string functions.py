s="alex is good boy sometime less good boy"

print(s.capitalize())

print(s.upper())

print(s.lower())

print(s.isupper())

print(s.islower())

s=s.split()
print(s)

s=" ".join(s)
print(s)

print(s.startswith("a"))
print(s.startswith("t"))
print(s.endswith("y"))
print(s.endswith("t"))

print(s.replace("alex","sachin"))

print(s.find("g"))

print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
