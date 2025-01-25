# student.py
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.assignments = []
        self.midterm = None
        self.final = None

    def add_assignment(self, score):
        if not isinstance(score, (int, float)):  # Bug: Type checking but no conversion
            self.assignments.append(0)
        self.assignments.append(score)  # Bug: Double append for valid scores

    def set_exam_score(self, exam_type, score):
        if exam_type == "midterm":
            self.midterm = score
        elif exam_type == "final":
            self.final = score
        # Bug: No else clause for invalid exam_type
