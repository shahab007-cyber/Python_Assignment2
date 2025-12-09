"""
Subject model class for managing subject information.
"""


class Subject:
    """Represents a subject/course in the system."""
    
    def __init__(self, subject_id: str, name: str, code: str, credits: int = None):
        """
        Initialize a Subject object.
        
        Args:
            subject_id: Unique identifier for the subject
            name: Subject name
            code: Subject code (e.g., CS101)
            credits: Number of credits (optional)
        """
        self.subject_id = subject_id
        self.name = name
        self.code = code
        self.credits = credits
    
    def __str__(self):
        """Return string representation of the subject."""
        credits_str = f", Credits: {self.credits}" if self.credits else ""
        return f"ID: {self.subject_id}, Code: {self.code}, Name: {self.name}{credits_str}"
    
    def __repr__(self):
        """Return detailed string representation."""
        return f"Subject(id={self.subject_id}, code={self.code}, name={self.name}, credits={self.credits})"
    
    def to_dict(self):
        """Convert subject to dictionary format for saving."""
        return {
            'subject_id': self.subject_id,
            'name': self.name,
            'code': self.code,
            'credits': str(self.credits) if self.credits else ''
        }
    
    @staticmethod
    def from_dict(data: dict):
        """Create a Subject object from a dictionary."""
        credits = int(data['credits']) if data.get('credits') and data['credits'].strip() else None
        return Subject(
            subject_id=data['subject_id'],
            name=data['name'],
            code=data['code'],
            credits=credits
        )
    
    @staticmethod
    def load_from_file(filepath: str):
        """
        Load all subjects from a text file.
        
        Args:
            filepath: Path to the subjects data file
            
        Returns:
            List of Subject objects
        """
        subjects = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split('|')
                    if len(parts) >= 3:
                        subject_id = parts[0].strip()
                        code = parts[1].strip()
                        name = parts[2].strip()
                        credits = int(parts[3].strip()) if len(parts) > 3 and parts[3].strip() else None
                        subjects.append(Subject(subject_id, code, name, credits))
        except FileNotFoundError:
            # File doesn't exist yet, return empty list
            pass
        except Exception as e:
            print(f"Error loading subjects: {e}")
        return subjects
    
    @staticmethod
    def save_to_file(subjects: list, filepath: str):
        """
        Save all subjects to a text file.
        
        Args:
            subjects: List of Subject objects to save
            filepath: Path to save the subjects data file
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("# Subject ID | Code | Name | Credits\n")
                for subject in subjects:
                    credits_str = str(subject.credits) if subject.credits else ''
                    f.write(f"{subject.subject_id}|{subject.code}|{subject.name}|{credits_str}\n")
        except Exception as e:
            print(f"Error saving subjects: {e}")

