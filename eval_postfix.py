"""
This module solves the evaluation of postfix expression task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V
"""

# Using the infix_to_postfix provided in the task description
# Please remove the print statements in the infix_to_postfix function before using it
from infix_to_postfix_start import infix_to_postfix


def evaluate_postfix(expression: str) -> int:
    """
    Evaluate a postfix expression.

    Args:
        expression: A postfix expression

    Returns:
        int: The result of the expression
    """
    stack = []
    operators = {"+", "-", "*", "/", "%", "^"}

    for token in expression.split():
        if token.isdigit():  # If token is a number, push it on the stack
            stack.append(int(token))

        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Insufficient operands for operator " + token)

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)

            elif token == "*":
                stack.append(a * b)

            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(a // b)  # Integer division

            elif token == "%":
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(a % b)

            elif token == "^":
                stack.append(a**b)

        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack.pop()


def main() -> None:
    """
    Main function for the postfix expression evaluation program.
    """
    expressions = ["(1 + 2) * 3", " 2 * 3 - 4 + 8 * 2", "(6-9)*(3+4)^2"]
    try:
        for expression in expressions:
            postfix_expression = infix_to_postfix(expression)  # type: ignore
            print("Infix expression:", expression, "Postfix expression:", postfix_expression)
            result = evaluate_postfix(postfix_expression)
            print("Result:", result)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
