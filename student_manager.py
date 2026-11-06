"""
Student Record Management module.

The StudentManager class keeps student records in memory and provides
validated CRUD operations. Keeping the business logic separate from any
user interface makes the module straightforward to test.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    student_id: str
    name: str
    marks: float

    @property
    def grade(self) -> str:
        """Return a grade using the documented percentage boundaries."""
        if self.marks >= 90:
            return "A"
        if self.marks >= 80:
            return "B"
        if self.marks >= 70:
            return "C"
        if self.marks >= 60:
            return "D"
        if self.marks >= 40:
            return "E"
        return "F"


class StudentManager:
    """Manage student records with validation and predictable return values."""

    def __init__(self):
        self._students: dict[str, Student] = {}

    @staticmethod
    def _validate_id(student_id: str) -> str:
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID must be a non-empty string.")
        return student_id.strip()

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")
        return name.strip()

    @staticmethod
    def _validate_marks(marks: float) -> float:
        if isinstance(marks, bool) or not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a number.")
        value = float(marks)
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        return value

    def add_student(self, student_id: str, name: str, marks: float) -> Student:
        sid = self._validate_id(student_id)
        clean_name = self._validate_name(name)
        clean_marks = self._validate_marks(marks)
        if sid in self._students:
            raise ValueError(f"Student ID '{sid}' already exists.")
        student = Student(sid, clean_name, clean_marks)
        self._students[sid] = student
        return student

    def get_student(self, student_id: str) -> Optional[Student]:
        sid = self._validate_id(student_id)
        return self._students.get(sid)

    def list_students(self) -> list[Student]:
        return sorted(self._students.values(), key=lambda student: student.student_id)

    def update_student(self, student_id: str, *, name=None, marks=None) -> Student:
        sid = self._validate_id(student_id)
        existing = self._students.get(sid)
        if existing is None:
            raise KeyError(f"Student ID '{sid}' was not found.")

        # Validate every requested field before changing the stored record.
        new_name = existing.name if name is None else self._validate_name(name)
        new_marks = existing.marks if marks is None else self._validate_marks(marks)
        updated = Student(sid, new_name, new_marks)
        self._students[sid] = updated
        return updated

    def delete_student(self, student_id: str) -> Student:
        sid = self._validate_id(student_id)
        if sid not in self._students:
            raise KeyError(f"Student ID '{sid}' was not found.")
        return self._students.pop(sid)

    def count(self) -> int:
        return len(self._students)
