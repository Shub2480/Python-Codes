def tri(base,height):
    return 1/2*(base*height)

base,height=[int(x) for x in input("Enter base , height: ").split(",")]
print(tri(base,height))
