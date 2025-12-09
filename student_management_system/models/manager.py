"""
Manager class to handle all operations for the Student Management System.
"""

import os
from typing import List, Optional
from .student import Student
from .subject import Subject
from .record import Record


class StudentManager:
    """Manages all operations for students, subjects, enrollments, and records."""
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the StudentManager.
        
        Args:
            data_dir: Directory path where data files are stored
        """
        self.data_dir = data_dir
        self.students_file = os.path.join(data_dir, "students.txt")
        self.subjects_file = os.path.join(data_dir, "subjects.txt")
        self.enrollments_file = os.path.join(data_dir, "enrollments.txt")
        self.records_file = os.path.join(data_dir, "records.txt")
        
        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)
        
        # Load all data
        self.students = Student.load_from_file(self.students_file)
        self.subjects = Subject.load_from_file(self.subjects_file)
        self.records = Record.load_from_file(self.records_file)
    
    def save_all(self):
        """Save all data to files."""
        Student.save_to_file(self.students, self.students_file)
        Subject.save_to_file(self.subjects, self.subjects_file)
        Record.save_to_file(self.records, self.records_file)
    
    # Student operations
    def add_student(self, student_id: str, name: str, email: str, age: int = None) -> bool:
        """
        Add a new student to the system.
        
        Args:
            student_id: Unique identifier for the student
            name: Student's full name
            email: Student's email address
            age: Student's age (optional)
            
        Returns:
            True if student was added, False if student_id already exists
        """
        if self.get_student(student_id):
            return False
        student = Student(student_id, name, email, age)
        self.students.append(student)
        self.save_all()
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Get a student by ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def get_all_students(self) -> List[Student]:
        """Get all students."""
        return self.students
    
    # Subject operations
    def add_subject(self, subject_id: str, name: str, code: str, credits: int = None) -> bool:
        """
        Add a new subject to the system.
        
        Args:
            subject_id: Unique identifier for the subject
            name: Subject name
            code: Subject code (e.g., CS101)
            credits: Number of credits (optional)
            
        Returns:
            True if subject was added, False if subject_id already exists
        """
        if self.get_subject(subject_id):
            return False
        subject = Subject(subject_id, name, code, credits)
        self.subjects.append(subject)
        self.save_all()
        return True
    
    def get_subject(self, subject_id: str) -> Optional[Subject]:
        """Get a subject by ID."""
        for subject in self.subjects:
            if subject.subject_id == subject_id:
                return subject
        return None
    
    def get_all_subjects(self) -> List[Subject]:
        """Get all subjects."""
        return self.subjects
    
    # Enrollment operations
    def enroll_student(self, student_id: str, subject_id: str) -> bool:
        """
        Enroll a student in a subject.
        
        Args:
            student_id: ID of the student
            subject_id: ID of the subject
            
        Returns:
            True if enrollment was successful, False otherwise
        """
        if not self.get_student(student_id):
            return False
        if not self.get_subject(subject_id):
            return False
        
        # Check if already enrolled
        if self.get_record(student_id, subject_id):
            return False
        
        # Create a new record for enrollment
        record = Record(student_id, subject_id)
        self.records.append(record)
        self.save_all()
        return True
    
    def get_record(self, student_id: str, subject_id: str) -> Optional[Record]:
        """Get a record for a student and subject."""
        for record in self.records:
            if record.student_id == student_id and record.subject_id == subject_id:
                return record
        return None
    
    def get_student_records(self, student_id: str) -> List[Record]:
        """Get all records for a specific student."""
        return [record for record in self.records if record.student_id == student_id]
    
    # Grade operations
    def add_grade(self, student_id: str, subject_id: str, grade: float) -> bool:
        """
        Add or update a grade for a student in a subject.
        
        Args:
            student_id: ID of the student
            subject_id: ID of the subject
            grade: Grade/score (0-100)
            
        Returns:
            True if grade was added/updated, False otherwise
        """
        if grade < 0 or grade > 100:
            return False
        
        record = self.get_record(student_id, subject_id)
        if not record:
            # Create new record if enrollment doesn't exist
            if not self.get_student(student_id) or not self.get_subject(subject_id):
                return False
            record = Record(student_id, subject_id, grade=grade)
            self.records.append(record)
        else:
            record.grade = grade
        
        self.save_all()
        return True
    
    # Attendance operations
    def mark_attendance(self, student_id: str, subject_id: str, attended: bool, total_classes: int = None) -> bool:
        """
        Mark attendance for a student in a subject.
        
        Args:
            student_id: ID of the student
            subject_id: ID of the subject
            attended: True if student attended, False otherwise
            total_classes: Total number of classes (optional, will increment if not provided)
            
        Returns:
            True if attendance was marked, False otherwise
        """
        record = self.get_record(student_id, subject_id)
        if not record:
            # Create new record if enrollment doesn't exist
            if not self.get_student(student_id) or not self.get_subject(subject_id):
                return False
            record = Record(student_id, subject_id)
            self.records.append(record)
        
        if total_classes is not None:
            record.total_classes = total_classes
        
        if record.total_classes is None:
            record.total_classes = 1
        
        if attended:
            if record.attendance is None:
                record.attendance = 1
            else:
                record.attendance += 1
        else:
            if record.attendance is None:
                record.attendance = 0
        
        if total_classes is not None:
            record.total_classes = total_classes
        else:
            record.total_classes = max(record.total_classes, record.attendance)
        
        self.save_all()
        return True
    
    # Report operations
    def get_student_report(self, student_id: str) -> Optional[dict]:
        """
        Get a comprehensive report for a student.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Dictionary containing student information and all their records, or None if student not found
        """
        student = self.get_student(student_id)
        if not student:
            return None
        
        student_records = self.get_student_records(student_id)
        report = {
            'student': student,
            'records': []
        }
        
        for record in student_records:
            subject = self.get_subject(record.subject_id)
            report['records'].append({
                'subject': subject,
                'record': record
            })
        
        return report

