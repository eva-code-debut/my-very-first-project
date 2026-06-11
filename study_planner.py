print("Please enter the required data below.")

nb_exams = int(input("Enter the amount of exams/tests you have"))
exams= []
for i in range(nb_exams):
    name = input(f"Enter the exam's name : ")
    exams.append(name)

difficulties = []
for exam in exams: 
    difficulty = float(input(f"rate the defficulty of the {exam} exam on a scale from 1 to 10 : "))
    difficulties.append(difficulty) 

dates = []
for exam in exams: 
    date = (input(f"Enter your due date for the {exam} exam : "))
    dates.append(date) 

print("Resume")

for i in range(nb_exams):
    print(exams[i], "-",difficulties[i], "-", dates[i])
    
