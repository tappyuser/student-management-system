from typing import TypedDict, Optional, Required, NotRequired, Literal
from pydantic import TypeAdapter

# Student schema, this defines how the student_profiles is to be structured
StudentSchema: TypedDict = TypedDict("StudentSchema", {
    "name": str,
    "matric": str,
    "age": int,
    "cgpa": float,
    "is_active": bool,
    "courses": Optional[list[str]],
    "departmentInfo": Optional[tuple[str, str, int]]
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
        "age": 39,
        "cgpa": 3.2,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "Woods",
        "matric": "20/89AC098",
        "age": 38,
        "cgpa": 3.2,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "Yelena",
        "matric": "20/60AC086",
        "age": 23,
        "cgpa": 3.2,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "Mike",
        "matric": "20/60AC076",
        "age": 25,
        "cgpa": 3.2,
        "is_active": True,
        "courses": courses,
        "departmentInfo": ("Electrical/Electronics", "Faculty of Engineering", 2025)
    },
    {
        "name": "Micheal",
        "matric": "20/60AC122",
        "age": 19,
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
    },
    {
        "matric": "20/89AC098",
        "courses": courses,
        "scores": [10, 30, 53, 87]
    },
    {
        "matric": "20/60AC086",
        "courses": courses,
        "scores": [49, 18, 74, 62]
    },
    {
        "matric": "20/60AC122",
        "courses": courses,
        "scores": [40, 89, 77, 32]
    },
    {
        "matric": "20/60AC076",
        "courses": courses,
        "scores": [18, 52, 67, 90]
    }
]

student_validator: TypeAdapter = TypeAdapter(StudentProfilesSchema)
student_profiles: list[StudentSchema] = student_validator.validate_python(student_profiles)

result_validator: TypeAdapter = TypeAdapter(StudentResultsSchema)
student_results: list[ResultSchema] = result_validator.validate_python(student_results)

