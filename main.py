import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]
TOTAL_SUBJECTS = 5


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card


def load_all_report():
    current_directory = os.getcwd()
    directory = str(current_directory) + "/students"
    all_report_card = []

    for i in range(NUM_STUDENTS):
        report_card = load_report_card(directory, i)
        all_report_card.append(report_card)

    return all_report_card



def average_student_grade(all_report_card):
    
    all_grades = []
    
    for student in all_report_card:
        student_average_grade = (student["math"] + student["science"] + student["history"] + student["english"] + student["geography"]) / TOTAL_SUBJECTS
        all_grades.append(student_average_grade)
        
    average_of_all_students_grade = round(sum(all_grades) / len(all_grades), 2)

    return average_of_all_students_grade



def sorted_subject(all_report_card):
    subjects = {subject: [] for subject in SUBJECTS}
    for student in all_report_card:
       for key in subjects.keys():
           subjects[key].append(student[key])

    for subject, value in subjects.items():
        average_score = sum(value) / len(value)
        subjects[subject] = average_score
    
    sorted_subjects = sorted(subjects.items(), key=lambda x: x[1])

    return sorted_subjects

def sorted_grade(all_report_card):
    grades = {str(i): [] for i in range(1, 9)}

    for student in all_report_card:
        student_average_grade = (student["math"] + student["science"] + student["history"] + student["english"] + student["geography"]) / TOTAL_SUBJECTS
        student_grade = student["grade"]
        for key, value in grades.items():
            if key == str(student_grade):
                value.append(student_average_grade)
       
    for grade, value in grades.items():
        average_grade = sum(value) / len(value)
        grades[grade] = average_grade
    
    sorted_grades = sorted(grades.items(), key=lambda x: x[1])
    
    return sorted_grades

def sorted_student(all_report_card):
    all_students = {str(i): [] for i in range(NUM_STUDENTS)}
    

    for student in all_report_card:
        student_average_grade = (student["math"] + student["science"] + student["history"] + student["english"] + student["geography"]) / TOTAL_SUBJECTS
        student_id = student["id"]
        for key, value in all_students.items():
            if key == str(student_id):
                value.append(student_average_grade)

    sorted_students = sorted(all_students.items(), key=lambda x: x[1])
    
    return sorted_students

all_report_card = load_all_report()          
print(f"""
Average Student Grade: {average_student_grade(all_report_card)}
Hardest Subject: {sorted_subject(all_report_card)[0][0]}
Easiest Subject: {sorted_subject(all_report_card)[-1][0]}
Best Performing Grade: {sorted_grade(all_report_card)[-1][0]}
Worst Performing Grade: {sorted_grade(all_report_card)[0][0]}
Best Student ID: {sorted_student(all_report_card)[-1][0]}
Worst Student ID: {sorted_student(all_report_card)[0][0]}
""")


