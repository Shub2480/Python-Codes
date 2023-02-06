
dict1={}
n=int(input("Enter number of students"))
for i in range(n):
    name=input("Enter name:")
    dict1[name]={}

    dict1[name]["maths"]={}
    dict1[name]["history"]={}
    dict1[name]["science"]={}

    dict1[name]["SUM"]={}
    dict1[name]["PERCENTAGE"]={}

    math_marks=int(input("ENter maths marks out 100:"))
    history_marks=int(input("ENter history marks out of 100:"))
    science_marks=int(input("ENter science marks out of 100:"))

    dict1[name]["maths"]=math_marks
    dict1[name]["history"]=history_marks
    dict1[name]["science"]=science_marks

    sum=dict1[name]["maths"]+dict1[name]["history"]+dict1[name]["science"]
    percentage=(sum/300)*100
    dict1[name]["SUM"]=sum
    dict1[name]["PERCENTAGE"]=percentage
    


print("Name of students\t","Maths    \t","History \t","Science \t", "SUM \t","PERCENTAGE")


for i in dict1:
    print(i,end="\t\t\t  ")
    print(dict1[i]["maths"],end="\t\t")
    print(dict1[i]["history"],end="\t\t  ")
    print(dict1[i]["science"],end="\t\t")
    print(dict1[i]["SUM"],end="\t\t")
    print(dict1[i]["PERCENTAGE"],end="\t\t")
    print()