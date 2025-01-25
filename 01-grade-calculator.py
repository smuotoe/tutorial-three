def calculate_final_grade(assignments, midterm, final):
    """
    Calculate student's final grade with weights:
    - Assignments: 40%
    - Midterm: 25%
    - Final: 35%
    """
    # First debugging point: Type error when processing assignments
    assignment_grades = []
    for grade in assignments:
        processed_grade = grade + 0  # Will raise TypeError for string grades
        assignment_grades.append(processed_grade)

    avg_assignments = sum(assignment_grades) / len(assignments)
    final_grade = (avg_assignments * 0.4) + (midterm * 0.15) + (final * 0.35)

    return round(final_grade, 2)


def process_student_records(students_data):
    """Process multiple student records"""
    results = {}

    for student, data in students_data.items():
        grade = calculate_final_grade(
            data['assignments'],
            data['midterm'],
            data['final']
        )
        results[student] = grade

    return results


# Test data with two error cases
test_data = {
    "Alice": {
        "assignments": [85, "92", 78],
        "midterm": 88,
        "final": 95
    },
    "Charlie": {
        "assignments": [88, 92, 85],
        "midterm": 90
    }
}

if __name__ == "__main__":
    try:
        results = process_student_records(test_data)
        print("Final grades:", results)
    except Exception as e:
        print(f"An error occurred: {type(e).__name__} - {str(e)}")