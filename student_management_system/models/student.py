"""
Student model class for managing student information.
"""


class Student:
    """Represents a student in the system."""
    
    def __init__(self, student_id: str, name: str, email: str, age: int = None):
        """
        Initialize a Student object.
        
        Args:
            student_id: Unique identifier for the student
            name: Student's full name
            email: Student's email address
            age: Student's age (optional)
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.age = age
    
    def __str__(self):
        """Return string representation of the student."""
        age_str = f", Age: {self.age}" if self.age else ""
        return f"ID: {self.student_id}, Name: {self.name}, Email: {self.email}{age_str}"
    
    def __repr__(self):
        """Return detailed string representation."""
        return f"Student(id={self.student_id}, name={self.name}, email={self.email}, age={self.age})"
    
    def to_dict(self):
        """Convert student to dictionary format for saving."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'age': str(self.age) if self.age else ''
        }
    
    @staticmethod
    def from_dict(data: dict):
        """Create a Student object from a dictionary."""
        age = int(data['age']) if data.get('age') and data['age'].strip() else None
        return Student(
            student_id=data['student_id'],
            name=data['name'],
            email=data['email'],
            age=age
        )
    
    @staticmethod
    def load_from_file(filepath: str):
        """
        Load all students from a text file.
        
        Args:
            filepath: Path to the students data file
            
        Returns:
            List of Student objects
        """
        students = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split('|')
                    if len(parts) >= 3:
                        student_id = parts[0].strip()
                        name = parts[1].strip()
                        email = parts[2].strip()
                        age = int(parts[3].strip()) if len(parts) > 3 and parts[3].strip() else None
                        students.append(Student(student_id, name, email, age))
        except FileNotFoundError:
            # File doesn't exist yet, return empty list
            pass
        except Exception as e:
            print(f"Error loading students: {e}")
        return students
    
    @staticmethod
    def save_to_file(students: list, filepath: str):
        """
        Save all students to a text file.
        
        Args:
            students: List of Student objects to save
            filepath: Path to save the students data file
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("# Student ID | Name | Email | Age\n")
                for student in students:
                    age_str = str(student.age) if student.age else ''
                    f.write(f"{student.student_id}|{student.name}|{student.email}|{age_str}\n")
        except Exception as e:
            print(f"Error saving students: {e}")

