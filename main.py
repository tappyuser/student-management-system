"""
This is a student managment program
"""

from database import *
import re

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

#for profile in student_profiles:
#    for studentprofile in student_profiles:
#    for result in student_results:
#       if result['matric'] == profile['matric']: result['grade'] = gradestudent(profile)

def setstudentresult(studentprofile: StudentSchema) -> ResultSchema | None:
    """ This takes a studentprofile. Gets the result by allowing getting user input and then returns a ResultSchema """
    result: ResultSchema = dict()
    scores: str = input("Enter the student scores for the courses seperated by ,\n" + ', '.join(courses) + ": ")
    pattern = r'(\d{1,3},\s?){3}\d{1,3}'
    if not re.match(pattern, scores): return None

    scores = scores.split(',')
    
    result['matric'] = studentprofile['matric']
    result['courses'] = studentprofile['courses']
    result['scores'] = scores
    result['grades'] = gradestudent(studentprofile)

    return result


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

def getresult(studentprofile: StudentSchema) -> ResultSchema | None:
    for result in student_results:
        if result['matric'] == studentprofile['matric']:
            return result
    return None

def checkeligibility(studentprofile: StudentSchema) -> bool:
    for key, value in studentprofile.items():
        print(key.upper() + ': ', value)

    if studentprofile['cgpa'] >= 4.5:
        return True
    return False

def gettopperformer() -> StudentSchema | None:
    """ This gets the top performing student by getting which of the student has the highest cgpa and it retuns that student """
    cgpa: float = student_profiles[0]['cgpa'] 
    student_index: float = 0
    for index, student in enumerate(student_profiles): 
        current_cgpa = student['cgpa'] 
        if current_cgpa > cgpa:
            cgpa = current_cgpa
            student_index = index
    return student_profiles[student_index]

def main() -> None:
    print(f"""
================================================
       Student Academic Performance System
================================================

Loading student records
{student_profiles.__len__()} student profiles loaded successfully
------------------------------------------------
    Menu Options
    1. View all students
    2. Add new student
    3. Check eligibility for graduation
    4. Find top performer
    5. Exit
------------------------------------------------
          """)

    while True:
        try:
            choice: int = int(input("Enter your choice: "))
        except Exception as e:
            print (e)
        
        match choice:
            case 1:
                print("List of students:")
                for index, student in enumerate(student_profiles): print(index + 1, student['name'])
            
            case 2:
                student: StudentSchema = addstudent()
                student_profiles.append(student)

                student_result: ResultSchema = setstudentresult(student)
                student_results.append(student_result)
                print(student['name'], ' added.')
                print(student_results[-1])

            case 3:
                name: str = input('Enter the student name: ')
                for student in student_profiles:
                    if student['name'] == name: 
                        eligible: bool = checkeligibility(student)
                        if eligible: print(f"{student['name']} is eligible")
                        else: print(f"{student['name']} is not eligible")

            case 4:
                student: StudentSchema = gettopperformer()
                print(f'{student["name"]} is the top performer')

            case 5:
                break




if __name__ == '__main__': 
    main()
