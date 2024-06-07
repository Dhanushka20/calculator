# Simple Calculator

A simple graphical calculator application built using Python and Tkinter. This calculator performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division
- Clear (C) button to reset the input field
- Error handling for invalid expressions

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/simple-calculator.git
    cd simple-calculator
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install any necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    **Note:** Since Tkinter is a standard library module, it is not listed in `requirements.txt`.

## Usage

1. Run the calculator application:

    ```bash
    python calculator.py
    ```

2. The calculator window will appear. You can use the buttons to perform calculations.

## Code Overview

### `calculator.py`

The main script that contains the implementation of the calculator.

#### Main Functions

- `evaluate_expression()`: Evaluates the mathematical expression entered in the input field and displays the result. Handles exceptions for invalid expressions.
- `button_click(value)`: Updates the input field with the value of the button clicked.
- `clear_entry()`: Clears the input field.

#### UI Elements

- **Entry Field**: For displaying the current input and results.
- **Buttons**: Numeric and operation buttons to input expressions and perform calculations. Includes a clear button to reset the input field.

### Button Layout

- The buttons are laid out in a 4x4 grid with the following labels:
