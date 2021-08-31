student_score = {
    "Puja": 85,
    "Pratibha": 91,
    "Tanu": 90,
    "Aman": 75,
    "Tanya": 69,
    "Olay": 60,
    }

student_grade = {}

for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectation"
    elif score > 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"        
print(student_grade)
