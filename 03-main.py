# 03-main.py
from student import Student
from grade_calculator import GradeCalculator
from grade_validator import GradeValidator


def process_student_grades():
    calculator = GradeCalculator()
    students = {}

    # Create test students
    alice = Student(1, "Alice")
    alice.add_assignment(85)
    alice.add_assignment("92")  # Bug: String input
    alice.set_exam_score("midterm", 88)
    alice.set_exam_score("final", 95)
    students[alice.student_id] = alice

    bob = Student(2, "Bob")
    bob.set_exam_score("midterm", 75)
    bob.set_exam_score("final", 82)
    students[bob.student_id] = bob  # Bug: No assignments added

    # Process grades
    results = {}
    validator = GradeValidator()

    for student_id, student in students.items():
        if validator.validate_student_record(student):
            try:
                final_grade = calculator.calculate_final_grade(student)
                results[student.name] = final_grade
            except Exception as e:
                print(f"Error processing {student.name}: {e}")
        else:
            print(f"Invalid record for {student.name}")

    return results


if __name__ == "__main__":
    results = process_student_grades()
    print("Final Grades:", results)
