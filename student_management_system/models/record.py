"""
Record model class for managing grades and attendance.
"""


class Record:
    """Represents a student's record (enrollment, grades, attendance) for a subject."""
    
    def __init__(self, student_id: str, subject_id: str, grade: float = None, attendance: int = None, total_classes: int = None):
        """
        Initialize a Record object.
        
        Args:
            student_id: ID of the student
            subject_id: ID of the subject
            grade: Grade/score (0-100) (optional)
            attendance: Number of classes attended (optional)
            total_classes: Total number of classes (optional)
        """
        self.student_id = student_id
        self.subject_id = subject_id
        self.grade = grade
        self.attendance = attendance
        self.total_classes = total_classes
    
    def __str__(self):
        """Return string representation of the record."""
        grade_str = f", Grade: {self.grade}" if self.grade is not None else ""
        attendance_str = ""
        if self.attendance is not None and self.total_classes is not None:
            percentage = (self.attendance / self.total_classes * 100) if self.total_classes > 0 else 0
            attendance_str = f", Attendance: {self.attendance}/{self.total_classes} ({percentage:.1f}%)"
        return f"Student: {self.student_id}, Subject: {self.subject_id}{grade_str}{attendance_str}"
    
    def __repr__(self):
        """Return detailed string representation."""
        return f"Record(student_id={self.student_id}, subject_id={self.subject_id}, grade={self.grade}, attendance={self.attendance}/{self.total_classes})"
    
    def to_dict(self):
        """Convert record to dictionary format for saving."""
        return {
            'student_id': self.student_id,
            'subject_id': self.subject_id,
            'grade': str(self.grade) if self.grade is not None else '',
            'attendance': str(self.attendance) if self.attendance is not None else '',
            'total_classes': str(self.total_classes) if self.total_classes is not None else ''
        }
    
    @staticmethod
    def from_dict(data: dict):
        """Create a Record object from a dictionary."""
        grade = float(data['grade']) if data.get('grade') and data['grade'].strip() else None
        attendance = int(data['attendance']) if data.get('attendance') and data['attendance'].strip() else None
        total_classes = int(data['total_classes']) if data.get('total_classes') and data['total_classes'].strip() else None
        return Record(
            student_id=data['student_id'],
            subject_id=data['subject_id'],
            grade=grade,
            attendance=attendance,
            total_classes=total_classes
        )
    
    @staticmethod
    def load_from_file(filepath: str):
        """
        Load all records from a text file.
        
        Args:
            filepath: Path to the records data file
            
        Returns:
            List of Record objects
        """
        records = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split('|')
                    if len(parts) >= 2:
                        student_id = parts[0].strip()
                        subject_id = parts[1].strip()
                        grade = float(parts[2].strip()) if len(parts) > 2 and parts[2].strip() else None
                        attendance = int(parts[3].strip()) if len(parts) > 3 and parts[3].strip() else None
                        total_classes = int(parts[4].strip()) if len(parts) > 4 and parts[4].strip() else None
                        records.append(Record(student_id, subject_id, grade, attendance, total_classes))
        except FileNotFoundError:
            # File doesn't exist yet, return empty list
            pass
        except Exception as e:
            print(f"Error loading records: {e}")
        return records
    
    @staticmethod
    def save_to_file(records: list, filepath: str):
        """
        Save all records to a text file.
        
        Args:
            records: List of Record objects to save
            filepath: Path to save the records data file
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("# Student ID | Subject ID | Grade | Attendance | Total Classes\n")
                for record in records:
                    grade_str = str(record.grade) if record.grade is not None else ''
                    attendance_str = str(record.attendance) if record.attendance is not None else ''
                    total_classes_str = str(record.total_classes) if record.total_classes is not None else ''
                    f.write(f"{record.student_id}|{record.subject_id}|{grade_str}|{attendance_str}|{total_classes_str}\n")
        except Exception as e:
            print(f"Error saving records: {e}")

