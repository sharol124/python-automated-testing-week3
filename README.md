# Student Record Management — Automated Testing (YuvaIntern Week 3)

## Project objective
This project demonstrates a testable Python module for managing student records. It includes automated unit tests for adding, retrieving, listing, updating and deleting records, input validation, record-count consistency, and grade boundaries.

## Project structure
- `student_manager.py` — data model and student-management business logic.
- `test_student_manager.py` — 26 automated tests using Python's built-in `unittest`.
- `TEST_PLAN.md` — test strategy, case coverage, and execution notes.
- `Week3_Automated_Testing_Report.docx` — detailed submission report.

## Requirements
- Python 3.10 or later.
- No third-party packages are required.

## Run the application tests
Open a terminal in this folder and run:

```bash
python -m unittest -v
```

A successful run should finish with `Ran 26 tests` and `OK`.

To check Python syntax separately:

```bash
python -m py_compile student_manager.py test_student_manager.py
```

## Design decisions
The project separates business logic from the command-line interface. `StudentManager` owns the records and exposes small methods for each operation. Input validation is centralized in helper methods to avoid repeating validation rules. A dictionary keyed by student ID provides direct lookup and prevents duplicate identifiers. Updates validate all proposed values before replacing a record, so a failed update cannot leave partially changed data.

## Grade scale
- 90–100: A
- 80–89.99: B
- 70–79.99: C
- 60–69.99: D
- 40–59.99: E
- Below 40: F

## Test methodology
The module was implemented first and then tested with a systematic unit-test suite. This is a test-after-development approach rather than a claim of strict test-driven development. Tests are isolated with `setUp()`, which creates a fresh manager for each test. Both normal inputs and invalid/edge-case inputs are included.

## Manual verification checklist
1. Add a student with valid details and verify the returned record.
2. Try adding the same ID again and verify that `ValueError` is raised.
3. Try marks below 0, above 100, and non-numeric marks.
4. Retrieve an existing ID and a missing ID.
5. Update a student's marks, then try an invalid update and verify the original record remains unchanged.
6. Delete an existing student and confirm the count decreases.
7. Run the full automated suite and confirm all 26 tests pass.

## Limitations and possible future improvements
Records are held in memory and are reset when the Python process ends. A future version could add JSON/SQLite persistence, a CLI, logging, and additional integration tests. These features are intentionally outside this task's focus so the testable module remains small and self-contained.
