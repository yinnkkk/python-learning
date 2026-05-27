import numpy as np
import matplotlib.pyplot as plt
import json

def menu():
    while True:
        try:
            choice = int(input("1. show grades\n2. add grades\n3. average grade\n4. highest/lowest grade\n5. failed/passed amount\n6. full statistics\n7 quit\n Enter:"))
            if choice == 1:
                show_grades()
            if choice == 2:
                add_grades()
            if choice == 3:
                average_grade()
            if choice == 4:
                highest_lowest()
            if choice == 5:
                failed_passed()
            if choice == 6:
                statistics()
            if choice == 7:
                break
        except:
            print("Not a proper number")

def show_grades():
    grades_normal = load_grades()
    grades = np.array(grades_normal)

    if len(grades) > 0:
        print(grades)
    else:
        print("No grades to print.")

def average_grade():
    grades = load_grades
    print(f"The average grade is {np.mean(grades)}")
def add_grades():
    try:
        with open("grades.json", "r") as f:
            grades_normal = json.load(f)
            grades = np.array(grades_normal)
    except:
        grades = np.array([])
    while True:
        try:
            grade = int(input("Which grade would you like to add? (Enter any letter to stop adding grades)"))
            grades = np.append(grades, grade)
            grades_normal = grades.tolist()
            with open("grades.json", "w") as f:
                json.dump(grades_normal, f)
        except:
            return
        
    

def load_grades():
    try:
        with open("grades.json", "r") as f:
            grades_normal = json.load(f)
            grades = np.array(grades_normal)
            return grades
    except:
        grades_normal = []
        grades = np.array(grades_normal)
        return grades

if __name__ == "__main__":
    menu()

    
