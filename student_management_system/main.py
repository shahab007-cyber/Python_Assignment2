"""
Student Management System - Main Entry Point
A simple command-line interface for managing students, subjects, enrollments, grades, and attendance.
"""

import os
from models.manager import StudentManager


def print_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("    STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. Add Subject")
    print("3. Enroll Student")
    print("4. Add Grade")
    print("5. Mark Attendance")
    print("6. View Student Report")
    print("7. List All Students")
    print("8. List All Subjects")
    print("9. Exit")
    print("="*50)


def add_student(manager: StudentManager):
    """Handle adding a new student."""
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Error: Student ID cannot be empty.")
        return
    
    if manager.get_student(student_id):
        print(f"Error: Student with ID '{student_id}' already exists.")
        return
    
    name = input("Enter Student Name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return
    
    email = input("Enter Student Email: ").strip()
    if not email:
        print("Error: Student email cannot be empty.")
        return
    
    age_input = input("Enter Student Age (optional, press Enter to skip): ").strip()
    age = int(age_input) if age_input else None
    
    if manager.add_student(student_id, name, email, age):
        print(f"✓ Student '{name}' added successfully!")
    else:
        print(f"Error: Failed to add student.")


def add_subject(manager: StudentManager):
    """Handle adding a new subject."""
    print("\n--- Add New Subject ---")
    subject_id = input("Enter Subject ID: ").strip()
    if not subject_id:
        print("Error: Subject ID cannot be empty.")
        return
    
    if manager.get_subject(subject_id):
        print(f"Error: Subject with ID '{subject_id}' already exists.")
        return
    
    code = input("Enter Subject Code (e.g., CS101): ").strip()
    if not code:
        print("Error: Subject code cannot be empty.")
        return
    
    name = input("Enter Subject Name: ").strip()
    if not name:
        print("Error: Subject name cannot be empty.")
        return
    
    credits_input = input("Enter Credits (optional, press Enter to skip): ").strip()
    credits = int(credits_input) if credits_input else None
    
    if manager.add_subject(subject_id, name, code, credits):
        print(f"✓ Subject '{name}' ({code}) added successfully!")
    else:
        print(f"Error: Failed to add subject.")


def enroll_student(manager: StudentManager):
    """Handle enrolling a student in a subject."""
    print("\n--- Enroll Student in Subject ---")
    student_id = input("Enter Student ID: ").strip()
    if not manager.get_student(student_id):
        print(f"Error: Student with ID '{student_id}' not found.")
        return
    
    subject_id = input("Enter Subject ID: ").strip()
    if not manager.get_subject(subject_id):
        print(f"Error: Subject with ID '{subject_id}' not found.")
        return
    
    if manager.enroll_student(student_id, subject_id):
        student = manager.get_student(student_id)
        subject = manager.get_subject(subject_id)
        print(f"✓ {student.name} enrolled in {subject.name} successfully!")
    else:
        print(f"Error: Student is already enrolled in this subject or enrollment failed.")


def add_grade(manager: StudentManager):
    """Handle adding a grade for a student."""
    print("\n--- Add Grade ---")
    student_id = input("Enter Student ID: ").strip()
    if not manager.get_student(student_id):
        print(f"Error: Student with ID '{student_id}' not found.")
        return
    
    subject_id = input("Enter Subject ID: ").strip()
    if not manager.get_subject(subject_id):
        print(f"Error: Subject with ID '{subject_id}' not found.")
        return
    
    try:
        grade = float(input("Enter Grade (0-100): ").strip())
        if grade < 0 or grade > 100:
            print("Error: Grade must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Invalid grade. Please enter a number.")
        return
    
    if manager.add_grade(student_id, subject_id, grade):
        student = manager.get_student(student_id)
        subject = manager.get_subject(subject_id)
        print(f"✓ Grade {grade} added for {student.name} in {subject.name}!")
    else:
        print(f"Error: Failed to add grade.")


def mark_attendance(manager: StudentManager):
    """Handle marking attendance for a student."""
    print("\n--- Mark Attendance ---")
    student_id = input("Enter Student ID: ").strip()
    if not manager.get_student(student_id):
        print(f"Error: Student with ID '{student_id}' not found.")
        return
    
    subject_id = input("Enter Subject ID: ").strip()
    if not manager.get_subject(subject_id):
        print(f"Error: Subject with ID '{subject_id}' not found.")
        return
    
    attended_input = input("Did the student attend? (y/n): ").strip().lower()
    attended = attended_input == 'y' or attended_input == 'yes'
    
    total_classes_input = input("Enter total classes (optional, press Enter to auto-increment): ").strip()
    total_classes = int(total_classes_input) if total_classes_input else None
    
    if manager.mark_attendance(student_id, subject_id, attended, total_classes):
        student = manager.get_student(student_id)
        subject = manager.get_subject(subject_id)
        status = "present" if attended else "absent"
        print(f"✓ Attendance marked as {status} for {student.name} in {subject.name}!")
    else:
        print(f"Error: Failed to mark attendance.")


def view_report(manager: StudentManager):
    """Handle viewing a student report."""
    print("\n--- Student Report ---")
    student_id = input("Enter Student ID: ").strip()
    
    report = manager.get_student_report(student_id)
    if not report:
        print(f"Error: Student with ID '{student_id}' not found.")
        return
    
    student = report['student']
    records = report['records']
    
    print("\n" + "="*60)
    print(f"STUDENT REPORT: {student.name}")
    print("="*60)
    print(f"Student ID: {student.student_id}")
    print(f"Email: {student.email}")
    if student.age:
        print(f"Age: {student.age}")
    print("\n" + "-"*60)
    print("ENROLLMENTS & RECORDS")
    print("-"*60)
    
    if not records:
        print("No enrollments found.")
    else:
        for item in records:
            subject = item['subject']
            record = item['record']
            print(f"\nSubject: {subject.name} ({subject.code})")
            if record.grade is not None:
                print(f"  Grade: {record.grade}")
            else:
                print(f"  Grade: Not assigned")
            
            if record.attendance is not None and record.total_classes is not None:
                percentage = (record.attendance / record.total_classes * 100) if record.total_classes > 0 else 0
                print(f"  Attendance: {record.attendance}/{record.total_classes} ({percentage:.1f}%)")
            else:
                print(f"  Attendance: Not recorded")
    
    print("\n" + "="*60)


def list_students(manager: StudentManager):
    """List all students."""
    print("\n--- All Students ---")
    students = manager.get_all_students()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"  {student}")


def list_subjects(manager: StudentManager):
    """List all subjects."""
    print("\n--- All Subjects ---")
    subjects = manager.get_all_subjects()
    if not subjects:
        print("No subjects found.")
    else:
        for subject in subjects:
            print(f"  {subject}")


def main():
    """Main function to run the Student Management System."""
    print("Initializing Student Management System...")
    # Get the directory where main.py is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "data")
    manager = StudentManager(data_dir)
    print("System ready!")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            add_student(manager)
        elif choice == '2':
            add_subject(manager)
        elif choice == '3':
            enroll_student(manager)
        elif choice == '4':
            add_grade(manager)
        elif choice == '5':
            mark_attendance(manager)
        elif choice == '6':
            view_report(manager)
        elif choice == '7':
            list_students(manager)
        elif choice == '8':
            list_subjects(manager)
        elif choice == '9':
            print("\nThank you for using Student Management System!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

