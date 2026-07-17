# Matrix Operations Tool

## Overview
The **Matrix Operations Tool** is a Python application developed using the **NumPy** library to perform fundamental matrix calculations through an interactive, menu-driven interface. It enables users to input matrices of different sizes and execute common mathematical operations efficiently while displaying results in a clear and structured format.

## Description
This project demonstrates how NumPy simplifies matrix manipulation in Python. Users can enter one or two matrices depending on the selected operation, and the program validates matrix dimensions before performing calculations. The application is designed to be simple, interactive, and suitable for learning the basics of matrix operations and numerical computing.

## Features
- Matrix Addition
- Matrix Subtraction
- Matrix Multiplication
- Matrix Transpose
- Determinant Calculation for square matrices
- Interactive menu-driven interface
- Input validation for matrix dimensions
- Structured display of matrices and results
- Error handling for incompatible operations

## Technologies Used
- Python 3
- NumPy

## Project Structure
```
MatrixOperationsTool/
│── matrix_operations.py
└── README.md
```

## Installation

1. Install Python 3.
2. Install NumPy:

```bash
pip install numpy
```

## Usage

Run the program from the terminal:

```bash
python matrix_operations.py
```

Choose an operation from the menu, enter the required matrix dimensions and elements, and the program will display the computed result.

## Supported Operations

| Operation | Description |
|----------|-------------|
| Addition | Adds two matrices of the same dimensions. |
| Subtraction | Subtracts one matrix from another of the same dimensions. |
| Multiplication | Multiplies two compatible matrices. |
| Transpose | Converts rows into columns. |
| Determinant | Calculates the determinant of a square matrix. |

## Sample Output

```
========================================
        MATRIX OPERATIONS TOOL
========================================
1. Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
4. Matrix Transpose
5. Matrix Determinant
6. Exit
```

## Learning Outcomes

This project helps in understanding:
- Matrix manipulation using NumPy
- Function-based program design
- Interactive console applications
- Matrix dimension validation
- Basic numerical computing with Python

## Conclusion

The Matrix Operations Tool provides a simple and efficient way to perform essential matrix calculations. It serves as an excellent beginner project for learning Python, NumPy, and mathematical computing concepts.
