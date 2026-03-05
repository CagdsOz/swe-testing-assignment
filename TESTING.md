# Testing Strategy

This project uses **unit testing** and **integration testing** to ensure the correctness and reliability of the Quick-Calc application.

---

## Unit Testing

Unit tests verify individual calculator functions, including:
- Addition
- Subtraction
- Multiplication
- Division
- Clear function

Edge cases covered:
- Division by zero
- Negative numbers
- Decimal numbers

Unit tests are executed using **Pytest** and can be run with:
```bash
pytest
Integration Testing

Integration tests verify the interaction between the input layer and the calculator logic. Examples include:

Entering 5, pressing +, entering 3, pressing =, and asserting the result is 8

Pressing Clear after a calculation resets the display to 0

Testing Approach

The test suite follows the Testing Pyramid:

Most tests are unit tests (base of the pyramid)

Fewer integration tests (middle layer)

Black-box vs White-box Testing:

Unit tests use white-box testing (internal logic is tested)

Integration tests use black-box testing (simulate user interaction without inspecting internal logic)

Functional vs Non-Functional Testing:

Only functional testing is performed (verifying arithmetic operations)

Non-functional aspects (performance, UI, scalability) are not tested

Regression Testing:

The test suite can be rerun after future changes to ensure no existing functionality breaks

Test Results Summary
Test Name	Type	Status
test_add	Unit	Pass
test_subtract	Unit	Pass
test_multiply	Unit	Pass
test_divide	Unit	Pass
test_clear	Unit	Pass
test_divide_by_zero	Unit	Pass
test_negative_numbers	Unit	Pass
test_decimal_numbers	Unit	Pass
test_full_addition_flow	Integration	Pass
test_clear_integration	Integration	Pass

This testing strategy demonstrates a comprehensive understanding of software testing concepts covered in Lecture 3 while ensuring Quick-Calc is reliable and correct.