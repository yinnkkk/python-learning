import numpy as np
import matplotlib.pyplot as plt
import json

def menu():
    while True:
        try:
            choice = int(input("1. show grades\n2. add grades\n3. average grade\n4. highest/lowest grade\n5. failed/passed amount\n6. full statistics\n7. Delete grades\n8. Quit\n Enter: "))
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
                delete_grades()
            if choice == 8:
                break
        except ValueError:
            print("Not a proper number")

def show_grades():
    grades_normal = load_grades()
    grades = np.array(grades_normal)

    if len(grades) > 0:
        for index, grade in enumerate(grades_normal(), start=1):
            print(f"{index}. {grade}")
    else:
        print("No grades to print.")

def average_grade():
    grades = load_grades()
    print(f"The average grade is {np.mean(grades)}")

def highest_lowest():
    grades = load_grades()
    print(f"Highest grade: {np.max(grades)}\nLowest grade: {np.min(grades)}")


def add_grades():
    try:
        with open("grades.json", "r") as f:
            grades_normal = json.load(f)
            grades = np.array(grades_normal)
    except:
        grades = np.array([])
    while True:
        try:
            grade = int(input("Which grade would you like to add? (Enter any letter to stop adding grades): "))
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

def delete_grades():
    grades = load_grades()
    show_grades()
    try:
        delete = int(input("Which grade would you like to delete? (Type the number): ") - 1)
        grade_deleted = grades[delete]
        grades = np.delete(grades, delete)
        grades_normal = grades.tolist()
        with open("grades.json", "w") as f:
            json.dump(grades_normal, f)
        print(f"{grade_deleted} succesfully deleted")
    except:
        print("Invalid entry.")

def failed_passed():
    grades = load_grades()
    failed = grades[grades < 5]
    print(f"Failed grades: {len(failed)}")
    print(f"Passed grades: {len(grades) - len(failed)}")

def statistics():
    grades = load_grades()
    failed = grades[grades < 5]
    print(f"Amount of grades: {len(grades)}\nAverage grade: {np.mean(grades)}\nHighest grade: {np.max(grades)}\nLowest grade: {np.min(grades)}\nMedian grade: {np.median(grades)}\nStandard Derivation: {np.std(grades)}\nFailed grades: {len(failed)}\nPassed grades: {len(grades)-len(failed)}\nSorted: {np.sort(grades)}")






if __name__ == "__main__":
    menu()

    
