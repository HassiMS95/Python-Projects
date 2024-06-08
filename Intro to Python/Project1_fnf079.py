# Header
# UTSA – Fall 2022 - CS1063 – Section 001 - Project 1 - written by Hassan Sheikh

#!/usr/bin/python
from string import *

# Lists all the exam grades for each student
def listGrades(d):
    print("List of Student Grades:\n")
    for key in d:
        print(f"{key}'s exam grade is {d[key]}\n")
    return None

# Displays how many A's, B's, C's, D's, and F's there are for the exam scores
def report(d):
    aCount = 0
    bCount = 0
    cCount = 0
    dCount = 0
    fCount = 0
    print("Report of Grades \n")
    # Logic for determining letter grades
    for key in d:
        if d[key] >= 90 and d[key] <= 100:
            aCount += 1
        elif d[key] >= 80 and d[key] <= 90:
            bCount += 1
        elif d[key] >= 70 and d[key] <= 80:
            cCount += 1
        elif d[key] >= 60 and d[key] <= 70:
            dCount += 1
        else:
            fCount += 1
    print("A:", aCount, "\n")
    print("B:", bCount, "\n")
    print("C:", cCount, "\n")
    print("D:", dCount, "\n")
    print("F:", fCount, "\n")
    return None

# Modifies the test grades for a selected student
def modifyGrades(d):
    gradeChange = ""
    selectedName = input("Please provide the name of the student: ")
    # Checks if the selected name matches wtth any of the names in the list of students
    if selectedName in d:
        newGrade = int(input("Please provide the new exam grade: "))
        d[selectedName] = newGrade
    else:
        print("Invalid Name, please resubmit: ")
        return None
        
    # Returns the new updated score for selected student
    gradeChange = print(f"{selectedName}\'s new exam grade is {d[selectedName]}.")
    return gradeChange


def main():
    i = 0
    classRoster = {}
    classSize = int(input("Please, enter the class size: "))
    # Logic for noting down the students and their grades
    while i < classSize:
    	studentName = input("Please, enter the student name: ")
    	studentGrade = int(input("Please, enter the student grade: "))
    	classRoster[studentName] = studentGrade
    	i += 1
    # Temporary value to start following while loop
    newValue = 0
    # while loop for the main part of the project based on the functions defined above
    while (newValue > -1):
        print("Main Menu\n\n1 - List Student Grades. 2 - Report of Grades. 3 - Modify a Grade. 4 - Exit Program\n\n")
        choice = int(input("Selection an Option: "))
        if choice == 1:
            listGrades(classRoster)
            continue
        elif choice == 2:
            report(classRoster)
            continue
        elif choice == 3:
            modifyGrades(classRoster)
            continue
        elif choice == 4:
        	# Exits out of the program
            print("Thank you. This program is brought to you by Python Expert: Hassan Sheikh.")
            return None
            # Exits out of the loop, thus ending the program
            break
        else:
        	# Logic for choosing incorrect integer value
            print("Value is out of range, please resubmit: ")
            continue

# Runs the main program
main()

# Footer
# UTSA – Fall 2022 - CS1063 – Section 001 - Project 1 - written by Hassan Sheikh