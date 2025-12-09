# Student Management System

A comprehensive Python-based Student Management System built using Object-Oriented Programming (OOP) principles. This system allows you to manage students, subjects, enrollments, grades, and attendance through a simple command-line interface.

## Features

- **Student Management**: Add and manage student information (ID, name, email, age)
- **Subject Management**: Add and manage subjects/courses (ID, code, name, credits)
- **Enrollment**: Enroll students in subjects
- **Grade Management**: Add and update grades for students in their enrolled subjects
- **Attendance Tracking**: Mark and track student attendance
- **Student Reports**: Generate comprehensive reports showing all student information, enrollments, grades, and attendance
- **Data Persistence**: All data is saved to and loaded from text files

## Project Structure

```
student_management_system/
├── main.py                 # Main entry point with menu system
├── models/                 # Model classes
│   ├── __init__.py
│   ├── student.py         # Student model class
│   ├── subject.py          # Subject model class
│   ├── record.py           # Record model for grades and attendance
│   └── manager.py         # Manager class for all operations
├── data/                   # Data storage directory
│   ├── students.txt       # Student data
│   ├── subjects.txt       # Subject data
│   ├── enrollments.txt    # Enrollment info (auto-maintained)
│   └── records.txt        # Grades and attendance records
└── README.md              # This file
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone or download this repository
2. Navigate to the `student_management_system` directory
3. Run the application:

```bash
python main.py
```

## Usage

### Main Menu Options

1. **Add Student**: Create a new student profile with ID, name, email, and optional age
2. **Add Subject**: Create a new subject/course with ID, code, name, and optional credits
3. **Enroll Student**: Enroll an existing student in a subject
4. **Add Grade**: Add or update a grade (0-100) for a student in a subject
5. **Mark Attendance**: Mark attendance for a student in a subject
6. **View Student Report**: Display a comprehensive report for a specific student
7. **List All Students**: Display all registered students
8. **List All Subjects**: Display all available subjects
9. **Exit**: Exit the application

### Example Workflow

1. Add a student:
   - Student ID: `S001`
   - Name: `John Doe`
   - Email: `john.doe@example.com`
   - Age: `20`

2. Add a subject:
   - Subject ID: `SUB001`
   - Code: `CS101`
   - Name: `Introduction to Computer Science`
   - Credits: `3`

3. Enroll the student:
   - Student ID: `S001`
   - Subject ID: `SUB001`

4. Add a grade:
   - Student ID: `S001`
   - Subject ID: `SUB001`
   - Grade: `85`

5. Mark attendance:
   - Student ID: `S001`
   - Subject ID: `SUB001`
   - Attended: `y` (yes)

6. View report:
   - Student ID: `S001`

## Data Storage

All data is stored in text files within the `data/` directory:

- **students.txt**: Stores student information (pipe-delimited format)
- **subjects.txt**: Stores subject information (pipe-delimited format)
- **records.txt**: Stores enrollment, grade, and attendance records (pipe-delimited format)

The system automatically creates the `data/` directory if it doesn't exist and handles file I/O operations transparently.

## Design Principles

- **Object-Oriented Design**: Each entity (Student, Subject, Record) is represented as a class
- **Separation of Concerns**: Business logic is separated into model classes and a manager class
- **No Global Data**: All data is encapsulated within class instances
- **Clean Code**: Well-documented, readable code with clear method names
- **Data Persistence**: Automatic save/load functionality for all operations

## Code Structure

### Student Class (`models/student.py`)
- Represents a student entity
- Handles serialization/deserialization to/from text files
- Provides string representations for display

### Subject Class (`models/subject.py`)
- Represents a subject/course entity
- Handles serialization/deserialization to/from text files
- Provides string representations for display

### Record Class (`models/record.py`)
- Represents enrollment, grade, and attendance records
- Links students to subjects
- Handles serialization/deserialization to/from text files

### StudentManager Class (`models/manager.py`)
- Central manager for all system operations
- Handles CRUD operations for students, subjects, and records
- Manages data persistence
- Provides high-level methods for all features

### Main Module (`main.py`)
- Provides command-line interface
- Handles user input and menu navigation
- Calls appropriate manager methods based on user choices

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.

## Author

Created as a Student Management System project demonstrating OOP principles in Python.

