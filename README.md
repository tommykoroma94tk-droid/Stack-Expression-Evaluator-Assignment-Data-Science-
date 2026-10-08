# Expression Evaluator Using a Stack

**Student:** Joseph Tommy Koroma  
**Student ID:** 905005353  
**Class:** DIT1201F  
**Module:** Data Structures and Algorithms  

---

## Description

This program reads mathematical expressions from a text file, evaluates each one using a custom Stack data structure, and writes the results to another text file.

The expressions can include integers, the four basic arithmetic operators (+, -, *, /), and parentheses. The program correctly handles operator precedence, so multiplication and division are evaluated before addition and subtraction.

---

## Purpose

The purpose of this program is to demonstrate how a Stack can be used to evaluate mathematical expressions without relying on Python's built-in `eval()` function. This is a classic algorithm taught in data structures courses.

---

## Data Structure Used

**Stack** – a linear data structure that follows the **LIFO** (Last In, First Out) principle.

The last item pushed onto the stack is the first one to be popped off. Think of it like a stack of plates: you always take the top plate first.

The custom `Stack` class in `stack.py` wraps a Python list and provides these operations:

| Operation     | Description                                      |
|---------------|--------------------------------------------------|
| `push(item)`  | Adds an item to the top of the stack             |
| `pop()`       | Removes and returns the top item                 |
| `peek()`      | Returns the top item without removing it         |
| `is_empty()`  | Returns `True` if there are no items on the stack|

---

## How Expressions Are Evaluated

The evaluator uses **two stacks**:

1. **Values stack** – stores numbers (operands)
2. **Operators stack** – stores operators (+, -, *, /) and parentheses

The algorithm works by reading the expression left to right, one character at a time:

- **Numbers** are pushed directly onto the values stack.
- **Operators** are pushed onto the operators stack, but first any operators already on the stack with equal or higher precedence are applied. This ensures multiplication and division happen before addition and subtraction.
- **Opening parenthesis `(`** is pushed onto the operators stack as a marker.
- **Closing parenthesis `)`** causes operators to be applied until the matching `(` is found and discarded.

Applying an operator means:
1. Pop the operator from the operators stack.
2. Pop two numbers from the values stack.
3. Perform the calculation.
4. Push the result back onto the values stack.

At the end, any remaining operators on the stack are applied, and the final answer is the single value left on the values stack.

**Example – `3 + 5 * 2`:**

Because `*` has higher precedence than `+`, the `5 * 2` is calculated first, giving `10`. Then `3 + 10 = 13`.

**Example – `(2 + 3) * 4`:**

The parentheses force `2 + 3 = 5` to be evaluated first. Then `5 * 4 = 20`.

---

## Project File Structure

```
Data Structure/
│
├── stack.py      # Custom Stack class
├── main.py       # Main program – reads input, evaluates, writes output
├── input.txt     # Input expressions (separated by -----)
├── output.txt    # Results (generated when main.py is run)
└── README.md     # This file
```

---

## How to Run the Program

Make sure you have Python 3 installed.

1. Open a terminal or command prompt.
2. Navigate to the `Data Structure` folder.
3. Run:

```
python main.py
```

The program will read `input.txt`, evaluate the expressions, and write the results to `output.txt`.

---

## Example Input (`input.txt`)

```
3 + 5 * 2
-----
(8 / 4) + 7 * 2
-----
10 - (2 + 3) * 4
```

---

## Example Output (`output.txt`)

```
13
-----
16
-----
-10
```

---

## Testing Summary

The program was tested with the following expressions:

| Expression         | Expected | Result |
|--------------------|----------|--------|
| `3 + 5 * 2`        | 13       | 13     |
| `(8 / 4) + 7 * 2`  | 16       | 16     |
| `10 - (2 + 3) * 4` | -10      | -10    |
| `2 + 3`            | 5        | 5      |
| `6 * 7`            | 42       | 42     |
| `20 / 5`           | 4        | 4      |
| `2 + 3 * 4`        | 14       | 14     |
| `(2 + 3) * 4`      | 20       | 20     |
| `20 / (2 + 3)`     | 4        | 4      |
| `10 - 3 - 2`       | 5        | 5      |

Error cases were also tested:

| Case                        | Behaviour                          |
|-----------------------------|------------------------------------|
| Unclosed `(`                | Raises error: mismatched parentheses|
| Extra `)`                   | Raises error: unexpected `)`       |
| Division by zero            | Raises error: division by zero     |
| Empty expression            | Raises error: expression is empty  |
