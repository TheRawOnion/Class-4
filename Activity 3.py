print("Enter the amount of marks obtained in each four of these subjects: ")
math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
biology = int(input("Biology: "))
sum = math + english + science + biology
print("The total marks you gained is: ", sum)
percentage = (sum/400) * 100
print(end="The percentage of marks you gained is: ")
print(percentage, "%")
