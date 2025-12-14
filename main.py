from typing import TypedDict, Optional, Required, NotRequired, Literal
from pydantic import TypeAdapter

"""
This is a student managment program
"""

# Student schema, this defines how the student_profiles is to be structured
StudentSchema: TypedDict = TypedDict("StudentSchema", {
    "name": str,
    "matric": str,
    "age": int,
    "cgpa": float,
    "is_active": bool,
    "courses": list[str],
    "departmentInfo": tuple[str, str, int]
})

type gradeType = Literal['A', 'B', 'C', 'D', 'F']

ResultSchema: TypedDict = TypedDict("ResultSchema", {
    "matric": Required[Optional[str]], # could be of type str or None
    "courses": Required[list[str]],
    "scores": Required[list[int]],
    "grades": NotRequired[list[gradeType]]
})

type StudentProfilesSchema = list[StudentSchema]
type StudentResultsSchema = list[ResultSchema]

# Data of the students
courses: list[str] = ["ELE311", "ELE321", "ELE331", "ELE361"]
student_names: list[str] = []

student_profiles: list[StudentSchema] = [
    {
        "name": "John",
        "matric": "20/60AC223",
        "age": 38,
        "cgpa": 3.2,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    }
]

student_results: list[ResultSchema] = [
    {
        "matric": "20/60AC223",
        "courses": courses,
        "scores": [10, 30, 53, 87]
    }
]

student_validator: TypeAdapter = TypeAdapter(StudentProfilesSchema)
student_profiles: list[StudentSchema] = student_validator.validate_python(student_profiles)

result_validator: TypeAdapter = TypeAdapter(StudentResultsSchema)
student_results: list[ResultSchema] = result_validator.validate_python(student_results)


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
print(student_results)

