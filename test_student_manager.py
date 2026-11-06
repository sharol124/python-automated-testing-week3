import unittest

from student_manager import Student, StudentManager


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()

    # Add operation and input validation (8 tests)
    def test_add_valid_student(self):
        student = self.manager.add_student("S101", "Asha", 88)
        self.assertEqual(student.student_id, "S101")
        self.assertEqual(student.name, "Asha")
        self.assertEqual(student.marks, 88.0)

    def test_add_trims_id_and_name(self):
        student = self.manager.add_student(" S102 ", "  Ravi  ", 75)
        self.assertEqual(student.student_id, "S102")
        self.assertEqual(student.name, "Ravi")

    def test_add_duplicate_id_is_rejected(self):
        self.manager.add_student("S101", "Asha", 88)
        with self.assertRaises(ValueError):
            self.manager.add_student("S101", "Ravi", 70)

    def test_add_empty_id_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student(" ", "Asha", 88)

    def test_add_empty_name_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("S101", "  ", 88)

    def test_add_marks_below_zero_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("S101", "Asha", -1)

    def test_add_marks_above_100_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("S101", "Asha", 101)

    def test_add_non_numeric_marks_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("S101", "Asha", "eighty")

    # Read/list operations (4 tests)
    def test_get_existing_student(self):
        self.manager.add_student("S101", "Asha", 88)
        self.assertEqual(self.manager.get_student("S101").name, "Asha")

    def test_get_missing_student_returns_none(self):
        self.assertIsNone(self.manager.get_student("S999"))

    def test_list_students_is_sorted_by_id(self):
        self.manager.add_student("S103", "Mina", 70)
        self.manager.add_student("S101", "Asha", 88)
        self.manager.add_student("S102", "Ravi", 75)
        self.assertEqual(
            [s.student_id for s in self.manager.list_students()],
            ["S101", "S102", "S103"],
        )

    def test_empty_list_returns_empty_list(self):
        self.assertEqual(self.manager.list_students(), [])

    # Update operation (5 tests)
    def test_update_marks(self):
        self.manager.add_student("S101", "Asha", 60)
        updated = self.manager.update_student("S101", marks=95)
        self.assertEqual(updated.marks, 95.0)

    def test_update_name(self):
        self.manager.add_student("S101", "Asha", 60)
        updated = self.manager.update_student("S101", name="Anu")
        self.assertEqual(updated.name, "Anu")

    def test_update_both_fields(self):
        self.manager.add_student("S101", "Asha", 60)
        updated = self.manager.update_student("S101", name="Anu", marks=91)
        self.assertEqual((updated.name, updated.marks), ("Anu", 91.0))

    def test_update_missing_student_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.manager.update_student("S999", marks=80)

    def test_invalid_update_does_not_change_existing_record(self):
        original = self.manager.add_student("S101", "Asha", 60)
        with self.assertRaises(ValueError):
            self.manager.update_student("S101", name="New Name", marks=150)
        current = self.manager.get_student("S101")
        self.assertEqual(current, original)

    # Delete/count operations (3 tests)
    def test_delete_existing_student(self):
        self.manager.add_student("S101", "Asha", 88)
        deleted = self.manager.delete_student("S101")
        self.assertEqual(deleted.name, "Asha")
        self.assertIsNone(self.manager.get_student("S101"))

    def test_delete_missing_student_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.manager.delete_student("S999")

    def test_count_tracks_add_and_delete(self):
        self.assertEqual(self.manager.count(), 0)
        self.manager.add_student("S101", "Asha", 88)
        self.assertEqual(self.manager.count(), 1)
        self.manager.delete_student("S101")
        self.assertEqual(self.manager.count(), 0)

    # Grade boundaries (6 tests)
    def test_grade_a_boundary(self):
        self.assertEqual(Student("S1", "A", 90).grade, "A")

    def test_grade_b_boundary(self):
        self.assertEqual(Student("S1", "A", 80).grade, "B")

    def test_grade_c_boundary(self):
        self.assertEqual(Student("S1", "A", 70).grade, "C")

    def test_grade_d_boundary(self):
        self.assertEqual(Student("S1", "A", 60).grade, "D")

    def test_grade_e_boundary(self):
        self.assertEqual(Student("S1", "A", 40).grade, "E")

    def test_grade_f_below_40(self):
        self.assertEqual(Student("S1", "A", 39.99).grade, "F")


if __name__ == "__main__":
    unittest.main(verbosity=2)
