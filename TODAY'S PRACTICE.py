print("\n=======UNIVERSITY GRADING SYSTEM=======\n")
print()

name = input("What is your name?\n").strip().upper()

units = int(input("Enter the number of course units\n"))

total_marks = 0

for i in range(units):

    print("\nCourse Units: ", i + 1)


    try:
      marks = float(input("Enter your marks here: "))

      if marks < 0 and marks > 100:
       print("Please enter marks from 0 to 100")

      if marks >= 80:
       Grade = "A"
      elif marks >= 70:
       Grade = "B"
      elif marks >= 60:
       Grade = "C"
      elif marks >= 50:
       Grade = "D"
      else:
       Grade = "F"
      print("Grade: ", Grade)
    except Exception as e:
     print("Please enter a number not words!!")



     total_marks = total_marks + marks
average = total_marks / units

print("\n=========STUDENTS RESULTS==========\n")

print("Student name: \n", name)
print("Course units: \n", units)
print("Sudents Marks:\n ", marks)
print("Total Marks: \n ", total_marks)
print("Average Mark: \n", average)
print()
print("Wish you all the best, Thank you!")

if average >= 80:
    print("First class degree\n")
    print("Remarks: Excellent, Keep it up!\n")
elif average >= 60:
    print("Second class degree\n")
    print("Remarks: Good")
elif average >= 55:
    print("Second class lower\n")
    print("Remarks: Fairly Good, Aim higher!")
else:
    print("Third class\n")
    print("Remarks: Failed!!")

