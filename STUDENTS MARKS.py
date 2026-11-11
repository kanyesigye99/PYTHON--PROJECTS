print("\n=======MBARARA UNIVERSITY======")
print("Welcome to Student Marks")
name= input("What is your name?\n")
marks= float(input("Enter your marks:\n"))
if marks <0 or marks >100:
    print("Invalid marks! Marks range from 0 to 100")
elif marks >=80:
    print("Grade: A")
    print("Comment : Excellent")
elif marks >=70:
    print("Grade: B")
    print("Comment : Very Good")
elif marks >=60:
    print("Grade: C")
    print("Comment :  Good")
elif marks >=50:
    print("Grade: D")
    print("Comment : Pass")
else:
    print("Fail")