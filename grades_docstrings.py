import copy

students = {
    '1001': {'last_name': 'Newman', 'first_name': 'Mark', 'uniqname': 'mwnewman'},
    '1002': {'last_name': 'Kano', 'first_name': 'Tsuyoshi', 'uniqname': 'tkano'},
    '1003': {'last_name': 'Grill', 'first_name': 'Gabriel', 'uniqname': 'ggrill'},
    '1004': {'last_name': 'Chen', 'first_name': 'Kangning', 'uniqname': 'knchen'}
}

grades = {
    '1001': [90, 88, 75, 95],   
    '1002': [92, 99, 88, 100],
    '1003': [95, 88, 82, 100],
    '1004': [99, 92, 94, 98]
}

def compute_average(num_list):
    sum = 0
    num_items = 0
    for n in num_list:
        sum += n
        num_items += 1
    return sum/num_items

def calculate_student_averages(students, grades):
    '''calculate and keep each student's average

        takes a dictionary of students and a dictionary of grades,  
        calculates averages for each student, then adds the average
        to the student's record in the students dictionary.

        Parameters
        ----------
        students : dict
            student info, indexed by id {id: {student_info}}
            modified in place by adding each student's average 
            to their record (key = 'average') 
            
        grades : dict
            student grades, indexed by id {id: [list_of_grades]}

        Returns
        -------
        None
    '''

    for id in grades:
        students_copy[id]["average"] = compute_average(grades[id])


def find_student_with_highest_average(students, grades):
    '''find student with the best average grade in the class

        takes a dictionary of students and a dictionary of grades,  
        calculates averages for each student, then returns
        the info of the student with the highest average.

        Note: results are indeterminate in the case of two top students 
        tied for the highest average. 


        Parameters
        ----------
        students : dict
            student info, indexed by id {id: {student_info}}
        grades : dict
            student grades, indexed by id {id: [list_of_grades]}

        Returns
        -------
        dict
            the student info (name, email, etc.) of the student with the 
            highest average
    '''

    max = 0
    top_student = None

    calculate_student_averages(students, grades)
    for s in students.values():
        if s["average"] > max:
            max = s["average"]
            top_student = s
    return top_student

def compute_final_grades(grades):
    student_grades = {}
    for id in grades:
        student_grades[id] = compute_average(grades[id])
    return student_grades

def print_final_grades(students, final_grades):
    for id in final_grades:
        student = students[id]
        print(student['first_name'], student['last_name'], 'has', final_grades[id])

students = calculate_student_averages(students, grades)
top_student = find_student_with_highest_average(students, grades)
print("The top student is", top_student['first_name'], top_student['last_name'])

final_grades = compute_final_grades(grades)
print_final_grades(students, final_grades)