overall_score = int(300)
number_of_subjects = int(3)

studets_name = input("Enter your name: ")
students_age = input("Enter your age: ")
mathematics = int(input("Enter score: "))
english = int(input("Enter score: "))
computer_science = int(input("Enter score: "))
total_score = mathematics + english + computer_science
print(total_score)
average_score = total_score/number_of_subjects
print (average_score)
percentage_score= total_score/overall_score*100
print(percentage_score)
pass_mark = 50
if mathematics >= pass_mark:
   print("mathematics: Passed")
else:
   print("mathematics: Failed")
if english >= pass_mark:
   print("english: Passed")
else:
   print("english: Failed")
if computer_science >= pass_mark:
   print("computer: Passed")
else:
   print("computer: Failed")



