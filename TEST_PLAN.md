# Test Plan and Methodology

## 1. Scope
Verify the public behavior of `StudentManager` and the grade calculation on `Student`. The suite uses Python `unittest` and does not require network access, external data, a database, or third-party packages.

## 2. Test design
Each test starts with a fresh `StudentManager` instance through `setUp()`. Tests are grouped by behavior. Assertions verify returned values, stored state, and expected exceptions. Invalid-input tests ensure bad data is rejected before it can corrupt records.

## 3. Coverage matrix (26 tests)

| ID | Test | Expected result |
|---|---|---|
| T01 | Add valid student | Student object is returned with normalized marks |
| T02 | Trim ID and name | Leading/trailing spaces are removed |
| T03 | Duplicate ID | ValueError; original record is retained |
| T04 | Empty ID | ValueError |
| T05 | Empty name | ValueError |
| T06 | Marks below 0 | ValueError |
| T07 | Marks above 100 | ValueError |
| T08 | Non-numeric marks | ValueError |
| T09 | Retrieve existing ID | Correct student is returned |
| T10 | Retrieve missing ID | None is returned |
| T11 | List records | Records are sorted by ID |
| T12 | List with no records | Empty list is returned |
| T13 | Update marks | New marks are stored |
| T14 | Update name | New name is stored |
| T15 | Update both fields | Both new values are stored |
| T16 | Update missing ID | KeyError |
| T17 | Invalid update | Original record remains unchanged |
| T18 | Delete existing ID | Deleted record is returned and removed |
| T19 | Delete missing ID | KeyError |
| T20 | Count add/delete | Count reflects current records |
| T21 | Grade at 90 | A |
| T22 | Grade at 80 | B |
| T23 | Grade at 70 | C |
| T24 | Grade at 60 | D |
| T25 | Grade at 40 | E |
| T26 | Grade below 40 | F |

## 4. Why boundary tests matter
Grade thresholds and mark limits are common sources of off-by-one errors. Testing exact thresholds (90, 80, 70, 60, 40) confirms that each boundary belongs to the intended grade. Testing -1 and 101 confirms that invalid marks cannot enter the system.

## 5. State-integrity test
`test_invalid_update_does_not_change_existing_record` deliberately supplies a valid new name together with invalid marks. The operation must reject the update and preserve the original record. This checks that validation happens before mutation, not after a partial update.

## 6. Execution
Run from the project directory:

```bash
python -m unittest -v
```

The suite is deterministic and self-contained. Each test creates its own manager, so test order does not affect the result.

## 7. Methodology and limitations
The module was developed and then covered with tests (test-after-development). This report does not claim that tests were written first. The tests are unit-level tests of the module's public methods; no persistence layer or external service exists in this version, so database/API integration tests are not applicable.
