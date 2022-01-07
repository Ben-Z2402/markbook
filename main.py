""
Markbook Application
Group members: 
"""
from typing import Dict


def create_assignment(a:str, b:str, c:int)-> Dict:
    a = {
        'name': a,
        'due': b,
        'points': c,
    }
    print()
    for i in a.items():
        print(i)

def create_classroom(a:str, b:str, c:int, d:str, e:list, f:list):
    classroom_dict = {
        'course code': a,
        'course name': b,
        'period': c,
        'teacher': d,
        'student_list': e,
        'assignment_list': f
    }
    print()
    for i in classroom_dict.items():
        print(i)
    
    # need to incorporate the lists somehow


def calculate_average_mark(student: Dict) -> float:
    values = a.values()
    marks_sum = sum(values)
    divisor = (len(a))
    marks_sum /= divisor
    return marks_sum
    


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom
    
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom['student_list'].append(student)
    return classroom['student_list']


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom['student_list'].remove(student)
    return classroom['student_list']


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    for key in student:
        if key == 'first_name':
            first_name = input("Enter new first name: ")

        elif key == 'last_name':
            last_name = input("Enter new last name: ")

        elif key == 'grade':
            grade = input("Enter new grade: ")
        
        elif key == 'marks':
            marks = student['marks']
            mark = int(input("Enter a mark\n"))
            marks.append(mark)
        
    student['first_name'] = first_name
    student['last_name'] = last_name
    student['grade'] = grade
    student['marks'] = marks

    return student

def main():

    student_list = []
    assignment_list = []

    print('Create a Classroom')
    print()
    class_code = input('What is the class code?: ')
    class_name = input('What is the class name?: ')
    period = input('What period is the class?: ')
    teacher_name = input("What is the teacher's name?: ")

    classroom_dict = create_classroom(class_code, class_name, period, teacher_name, student_list, assignment_list)

    print()
    for i in classroom_dict.items():
            print(i)

    while True:
        print()
        print('[1] Create an Assignment')
        print('[2] Manipulate assignments')
        print('[3] Exit the program')
        print()

        print('List of Assignments:')
        assign_list = classroom_dict['assignment_list']
        print(*assign_list, sep= '\n')
        print()

        user_input = input('What would you like to do?: ')
        print()
        user_input = int(user_input)

        if user_input == 1:
            assign_name = input('Name the assignment: ')
            due_date = input('When is the assignment due?: ')
            points = input('How many points is the assignment worth? (denominator): ')
            created_assignment = create_assignment(assign_name, due_date, points)

            print()
            for i in created_assignment.items():
                print(i)

            assignment_list.append(created_assignment)

        elif user_input == 2:
            while True:
                print()
                print('[1] Edit and Assignment')
                print('[2] Delete an Assignment')
                print('[3] Back')
                print()

                user_input = input('What would you like to do?: ')
                print()
                user_input = int(user_input)

                if user_input == 1:
                    assign_list = classroom_dict['assignment_list']
                    print(*assign_list, sep= '\n')
                    print()

                    user_input = input('Which Assignment would you like to edit?: ')
                    print()

                    for assignment in assign_list:
                        if user_input == assignment.get('name'):

                            print(assignment)
                            print()

                            print('[1] Name')
                            print('[2] Due date')
                            print('[3] Points')
                            print('[4] Back')
                            print()

                            user_input = input('What would you like to change?: ')
                            user_input = int(user_input)
                            print()

                            if user_input == 1:
                                
                                user_input = input('What would you like to change the name to?: ')
                                assignment['name'] = user_input
                                print()
                                print(assignment)
                                print()

                            elif user_input == 2:
                                
                                user_input = input('What would you like to change the due date to?: ')
                                assignment['due'] = user_input
                                print()
                                print(assignment)
                                print()

                            elif user_input == 3:
                                
                                user_input = input('What would you like to change the points to?: ')
                                assignment['points'] = user_input
                                print()
                                print(assignment)
                                print()

                            elif user_input == 4:
                                break
                
                elif user_input == 2:
                    assign_list = classroom_dict['assignment_list']
                    print(*assign_list, sep= '\n')
                    print()

                    user_input = input('Which assignment would you like to delete?: ')

                    for assignment in assign_list:
                        if user_input == assignment.get('name'):
                            assign_list.remove(assignment)

                    print()
                    assign_list = classroom_dict['assignment_list']
                    print(*assign_list, sep= '\n')
                
                elif user_input == 3:
                    break
        
        elif user_input == 3:
            print('Shutting Down')
            break
                
        else:
            print('Not an option')

main()
