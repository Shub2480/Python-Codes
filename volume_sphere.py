def volume(r):
    return (4/3)*3.14*(r**3)

n=int(input(("Enter number: ")))
print("{:.2f}".format(volume(n)))