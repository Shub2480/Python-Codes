s=[x**3 for x in range(1,21)]
print(s)



s=[x for x in range(1,100) if x%2==0]
print(s)


library = [('book1',2002),('book2',2012),('book3',2007),('book4',2015),('book5',2005),('book6',2018)]

lib=[library[s] for s in range(len(library)) if library[s][1]>=2010]
print(lib)


