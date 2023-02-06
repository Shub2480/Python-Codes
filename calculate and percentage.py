maths=int(input("Enter your maths marks:"))
physics=int(input("Enter your physics marks:"))
history=int(input("Enter your history marks:"))
english=int(input("Enter your english marks:"))
chemistry=int(input("Enter your chemistry marks:"))

total_marks=(maths+physics+history+english+chemistry)

percentage=(total_marks*100)/250

print("your total score is",total_marks,"and percentage is",percentage)
