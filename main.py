# main.py
# Expression Evaluator using a custom Stack
# Student: Joseph Tommy Koroma
# Student ID: 905005353
# Class: DIT1201F

from stack import Stack


# ------------------------------------------------------------------
# Operator helpers
# ------------------------------------------------------------------

def precedence(op):
    """Return the precedence level of an operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def apply_operator(values, ops):
    """Pop one operator and two operands from the stacks,
    apply the operation, and push the result back onto values."""
    op = ops.pop()
    right = values.pop()
    left = values.pop()

    if op == '+':
        values.push(left + right)
    elif op == '-':
        values.push(left - right)
    elif op == '*':
        values.push(left * right)
    elif op == '/':
        if right == 0:
            raise ZeroDivisionError("Division by zero in expression.")
        # Use integer division only when the result is a whole number
        result = left / right
        values.push(int(result) if result == int(result) else result)


# ------------------------------------------------------------------
# Core evaluator
# ------------------------------------------------------------------

def evaluate(expression):
    """Evaluate a mathematical expression string using two stacks.

    Stack 1 (values)  – stores numbers (operands)
    Stack 2 (ops)     – stores operators and parentheses

    The algorithm:
      - Read each token left to right.
      - Numbers go straight onto the values stack.
      - Operators are pushed onto ops, but first any pending operators
        with equal or higher precedence are applied (this enforces
        correct precedence and left-to-right evaluation).
      - '(' is pushed as a marker onto ops.
      - ')' triggers applying operators until the matching '(' is found.
    """
    expression = expression.strip()

    if not expression:
        raise ValueError("Expression is empty.")

    values = Stack()
    ops = Stack()

    i = 0
    while i < len(expression):
        ch = expression[i]

        # Skip whitespace
        if ch == ' ':
            i += 1
            continue

        # Multi-digit (or single-digit) number
        if ch.isdigit():
            num_str = ''
            while i < len(expression) and expression[i].isdigit():
                num_str += expression[i]
                i += 1
            values.push(int(num_str))
            continue  # i already advanced

        # Opening parenthesis – push as marker
        elif ch == '(':
            ops.push(ch)

        # Closing parenthesis – apply until matching '('
        elif ch == ')':
            if ops.is_empty():
                raise ValueError("Mismatched parentheses: unexpected ')'.")
            while not ops.is_empty() and ops.peek() != '(':
                apply_operator(values, ops)
            if ops.is_empty():
                raise ValueError("Mismatched parentheses: no matching '('.")
            ops.pop()  # discard the '('

        # Operator
        elif ch in ('+', '-', '*', '/'):
            # Apply operators already on the stack that have >= precedence
            while (not ops.is_empty() and
                   ops.peek() != '(' and
                   precedence(ops.peek()) >= precedence(ch)):
                apply_operator(values, ops)
            ops.push(ch)

        else:
            raise ValueError(f"Unknown character in expression: '{ch}'")

        i += 1

    # Apply any remaining operators
    while not ops.is_empty():
        if ops.peek() == '(':
            raise ValueError("Mismatched parentheses: unclosed '('.")
        apply_operator(values, ops)

    if values.is_empty():
        raise ValueError("Expression produced no result.")

    return values.pop()


# ------------------------------------------------------------------
# File I/O
# ------------------------------------------------------------------

SEPARATOR = "-----"


def read_expressions(filename):
    """Read the input file and return a list of expression strings."""
    with open(filename, 'r') as f:
        content = f.read()

    # Split by the separator line
    parts = content.split(SEPARATOR)
    expressions = [part.strip() for part in parts]
    return expressions


def write_results(filename, results):
    """Write the results to the output file, separated by '-----'."""
    lines = []
    for i, result in enumerate(results):
        lines.append(str(result))
        if i < len(results) - 1:
            lines.append(SEPARATOR)

    with open(filename, 'w') as f:
        f.write('\n'.join(lines) + '\n')


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    print("Expression Evaluator")
    print("Student: Joseph Tommy Koroma")
    print("-" * 30)

    expressions = read_expressions(input_file)
    results = []

    for expr in expressions:
        if not expr:
            print("Skipping empty expression.")
            results.append("Error: empty expression")
            continue
        try:
            result = evaluate(expr)
            # Display as int if it is a whole number
            if isinstance(result, float) and result == int(result):
                result = int(result)
            print(f"  {expr}  =  {result}")
            results.append(result)
        except ZeroDivisionError as e:
            print(f"  {expr}  =>  Error: {e}")
            results.append(f"Error: {e}")
        except ValueError as e:
            print(f"  {expr}  =>  Error: {e}")
            results.append(f"Error: {e}")

    write_results(output_file, results)
    print("-" * 30)
    print(f"Results written to {output_file}")


if __name__ == '__main__':
    main()
