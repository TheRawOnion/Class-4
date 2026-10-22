Amount = int(input("Please enter the amount for withdrawal: "))
note1 = Amount // 100
note2 = (Amount % 100) // 50
note3 = ((Amount % 100) % 50) // 10
print("The number of $100 notes is: ", note1)
print("The number of $50 notes is: ", note2)
print("The number of $10 notes is: ", note3)