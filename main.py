"""
This is a student managment program
"""

from typing import Optional, Required, NotRequired, Literal
from database import *

def gradestudent(studentprofile: StudentSchema) -> list[gradeType]:
    """ This takes a student profile and grades the student based on the score """
    for result in student_results:
        if studentprofile['matric'] == result['matric']: break

    scores: list[int] = result['scores']
    grades: list[gradeType] = list() 

    for score in scores:
        if score >= 70 and score <= 100:
            grades.append('A')
        elif score >= 60 and score <= 69:
            grades.append('B')
        elif score >= 50 and score <= 59:
            grades.append('C')
        elif score >= 40 and score <= 49:
            grades.append('D')
        else:
            grades.append('F')
    return grades

def getfeedback(grade: gradeType) -> str:
    """ This function takes a grade like A, B or C and returns a string like 'Excellent', 'Very Good' ... """
    match grade:
        case 'A': return 'Excellent'
        case 'B': return 'Very Good'
        case 'C': return 'Good'
        case 'D': return 'Fair'
    return 'Poor'

for profile in student_profiles:
    for result in student_results:
        if result['matric'] == profile['matric']: result['grade'] = gradestudent(profile)

def addstudent() -> StudentSchema | None:
    """ This adds a student to the student_profiles table/database """
    student: StudentSchema = dict()
    name: str = input("Enter your name: ")
    matric: str = input("Enter your matric no: ")

    try:
        age: int = int(input("Enter your age (16 - 40): "))
        if not age >= 16 and age <= 40: 
            print("Age must be between 16 and 40")
    except Exception as e:
        print(e)

    try: 
        cgpa: float = float(input("Enter you CGPA (0.0 - 5.0): "))
        if not cgpa >= 0.0 and cgpa <= 5.0: 
            print("CGPA must be between 0.0 and 5.0")
    except Exception as e:
        print(e)

    department: str = input("Enter your department: ")
    faculty: str = input("Enter your faculty: ")
    year: int = int(input("Enter your year of admission: "))

    student['name'] = name
    student['age'] = age
    student['matric'] = matric
    student['is_active'] = True
    student['courses'] = courses
    student['departmentInfo'] = (department, faculty, year)

    return student

def main() -> None:
    print(addstudent())

if __name__ == '__main__': 
    main()
