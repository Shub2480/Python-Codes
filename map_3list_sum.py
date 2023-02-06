input_list_1 = [3, 4, 5, 6]
input_list_2 = [1, 8, 4, 9]
input_list_3 = [13, 14, 15, 10]

new=list(map(lambda a,b,c: a+b+c,input_list_1,input_list_2,input_list_3))

print(new)