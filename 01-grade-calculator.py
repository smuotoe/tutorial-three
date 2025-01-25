def calculate_final_grade(assignments, midterm, final):
    """
    Calculate student's final grade with weights:
    - Assignments: 40%
    - Midterm: 25%
    - Final: 35%
    """
    assignment_grades = []
    for grade in assignments:
        if grade > 100:
            grade = 100
        assignment_grades.append(grade)

    # Bug: Division by zero potential
    avg_assignments = sum(assignment_grades) / len(assignments)

    # Bug: Wrong weight application
    final_grade = (avg_assignments * 0.4) + (midterm * 0.15) + (final * 0.35)

    return round(final_grade, 2)


def process_student_records(students_data):
    """Process multiple student records"""
    results = {}

    for student, data in students_data.items():
        # Bug: KeyError potential
        grade = calculate_final_grade(
            data["assignments"], data["midterm"], data["final"]
        )
        results[student] = grade

    return results


# Test data
test_data = {
    "Alice": {"assignments": [85, 92, 78, 105], "midterm": 88, "final": 95},
    "Bob": {
        "assignments": [],
        "midterm": 75,
        "final": 82,
    },
    "Charlie": {"assignments": [88, 92, 85], "midterm": 90},
}

# Run the code
results = process_student_records(test_data)
print(results)
