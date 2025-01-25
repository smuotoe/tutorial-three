# grade_calculator.py
class GradeCalculator:
    def __init__(self):
        self.weights = {"assignments": 0.4, "midterm": 0.25, "final": 0.35}

    def calculate_assignment_average(self, assignments):
        if len(assignments) == 0:
            return 0  # Bug: Should raise exception
        return sum(assignments) / len(assignments)

    def calculate_final_grade(self, student):
        assignment_avg = self.calculate_assignment_average(student.assignments)
        # Bug: No None checks for midterm/final
        weighted_grade = (
            assignment_avg * self.weights["assignments"]
            + student.midterm * self.weights["midterm"]
            + student.final * self.weights["final"]
        )
        return round(weighted_grade, 2)
