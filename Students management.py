import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Student:
    def __init__(self, s_name, s_class, s_grade):
        self.s_name = s_name
        self.s_class = s_class
        self.s_grade = s_grade
        self.s_status = self._get_status(s_grade)

    def _get_status(self, grade):
        if grade >= 90: return 'Excellent'
        elif grade >= 75: return 'Very Good'
        elif grade >= 50: return 'Good'
        return 'Low'

    def print_report(self):
        print(f"Student: {self.s_name}")
        print(f"Class  : {self.s_class}")
        print(f"Grade  : {self.s_grade}%")
        print(f"Status : {self.s_status}")
        print("-" * 35)

class GradeSystem:
    def __init__(self):
        self.students_list = []

    def register_student(self):
        clear_screen()
        print("--- Register New Student ---")
        s_name = input("Enter student name: ").strip().title()
        s_class = input("Enter class/section: ").strip().upper()
        
        while True:
            try:
                s_grade = int(input("Enter student grade (0-100): "))
                if 0 <= s_grade <= 100:
                    break
                print("Error: Grade must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid number.")

        new_student = Student(s_name, s_class, s_grade)
        self.students_list.append(new_student)
        
        print("\nStudent record created successfully!")
        time.sleep(2)

    def show_records(self):
        clear_screen()
        if not self.students_list:
            print("Database is empty. No records to display.")
        else:
            print(f"STUDENT RECORDS - TOTAL: {len(self.students_list)}\n" + "="*35)
            for s in self.students_list:
                s.print_report()
        input("\nPress Enter to return to menu...")

    def search_student(self):
        clear_screen()
        if not self.students_list:
            print("No records available for search.")
            time.sleep(2)
            return

        query = input("Search by Student Name: ").lower()
        results = [s for s in self.students_list if query in s.s_name.lower()]
        
        print("\n--- Search Results ---")
        if results:
            for s in results:
                s.print_report()
        else:
            print("No student found with that name.")
        input("\nPress Enter to continue...")

    def main_menu(self):
        while True:
            clear_screen()
            print("      HUSSAM SCHOOL SYSTEM     ")
            print("===============================")
            print("1) Add New Student")
            print("2) Display All Records")
            print("3) Search for Student")
            print("4) Exit System")
            print("===============================")
            
            cmd = input("Select Option: ")

            if cmd == '1':
                self.register_student()
            elif cmd == '2':
                self.show_records()
            elif cmd == '3':
                self.search_student()
            elif cmd == '4':
                print("\nExiting System...")
                break
            else:
                print("\nInvalid choice! Please try again.")
                time.sleep(1)

if __name__ == "__main__":
    school = GradeSystem()
    school.main_menu()
