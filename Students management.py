import time
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Student:
    def __init__(self, name, classs, grade, status):
        self.name = name
        self.classs = classs
        self.grade = grade
        self.status = status

    def print_info(self):
        print('_' * 20)
        print(f'Student name: {self.name}')
        print(f'Student class: {self.classs}')
        print(f'Student grade: {self.grade}')
        print(f'Student status: {self.status}')

def add_student():
    name = input('Enter the student name: ')
    classs = input('Enter the student class: ')
    while True:
        try:
            grade = int(input('Enter the student grade: '))
            if grade > 100:
                print('Error, please try again')
                continue
            else:
                if grade >= 90:
                    status = 'Excellent'
                elif grade >= 75:
                    status = 'Very good'
                elif grade >= 50:
                    status = 'Good'
                else:
                    status = 'Low'
            break
        except ValueError:
            print('Please enter a number')
    
    return Student(name, classs, grade, status)

students = []

while True:
    clear_screen()
    print('| Welcome to the students grade management |\n')
    choice = input('1. Add a new student\n2. Display all student\n3. Exiting\nEnter your choice: ')
    if choice not in ['1', '2', '3']:
        print('Error, Please choose from the options')
        time.sleep(2)
    
    elif choice == '1':
        time.sleep(1)
        clear_screen()
        students.append(add_student())
        print('\nStudent added successfully.')
        time.sleep(2)

    elif choice == '2':
        if students:
            time.sleep(1)
            clear_screen()
            print('Displaying students...\n')
            for student in students:
                time.sleep(2)
                student.print_info()
            print('\nDisplaying finished.')
            exit = input('Press enter to continue')
        else:
            print('Sorry, There is no students to display')
            time.sleep(2)
    else:
        print('\nExiting...')
        time.sleep(2)
        break
