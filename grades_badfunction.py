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


def do_grades(grades):
    for id in grades:
        sum = 0
        num_items = 0
        for n in grades[id]:
            sum += n
            num_items += 1
        students[id]["average"] = sum/num_items
    student_grades = {}
    for id in grades:
        sum = 0
        num_items = 0
        for n in grades[id]:
            sum += n
            num_items += 1
        student_grades[id] = sum/num_items
    for id in student_grades:
        student = students[id]
        print(student['first_name'], student['last_name'], 'has', student_grades[id])

do_grades(grades)
