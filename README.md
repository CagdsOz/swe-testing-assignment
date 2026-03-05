# Quick-Calc

Quick-Calc is a simple **command-line calculator** application that performs basic arithmetic operations such as **addition, subtraction, multiplication, and division**, and includes a **clear** function to reset the current input.

This project demonstrates **software testing practices**, including **unit testing** and **integration testing**, following concepts from Lecture 3 of Advanced Software Engineering.

---

## Setup Instructions

1. Make sure you have **Python 3.x** installed.
2. (Optional but recommended) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install required dependencies:

pip install pytest
Run Application

To run the calculator:

python main.py
Run Tests

Unit and integration tests are included. To run all tests:

pytest

All tests should pass successfully. The test suite covers:

Addition, Subtraction, Multiplication, Division (core operations)

Edge cases (division by zero, negative numbers, decimal numbers)

Testing Framework Research

For Python, two popular testing frameworks are Pytest and Unittest:

Pytest

Pros: Simple syntax, powerful fixtures, easy assertion handling, widely used in modern Python projects.

Cons: Slight learning curve for advanced features (fixtures, parametrization).

Unittest

Pros: Comes built-in with Python, familiar for developers with Java/JUnit background.

Cons: More verbose, less flexible, setup/teardown can be cumbersome.

Choice: Pytest was selected for this project due to its simplicity and powerful features, making it ideal for both unit and integration tests. Its clear syntax reduces boilerplate and improves readability of test cases.

Project Features

Addition, Subtraction, Multiplication, Division

Division by zero handled gracefully

Clear function resets the current input and result

Unit tests for each operation and edge cases

Integration tests simulate user interactions

Notes

This is a CLI-based calculator. GUI is not implemented, as the focus is on testing and code quality.

All functionality has been verified through tests and works as expected.