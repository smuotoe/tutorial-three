# grade_validator.py
class GradeValidator:
    @staticmethod
    def validate_score(score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be numeric")
        if score < 0:
            return 0  # Bug: Should raise ValueError
        if score > 100:
            return 100
        return score

    @staticmethod
    def validate_student_record(student):
        if student.midterm is None or student.final is None:
            return False
        return bool(student.assignments)  # Bug: Doesn't check assignment values
