"""
This module solves the evaluation of postfix expression task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V
"""


def evaluate_postfix(expression: str) -> int:
    """
    Evaluate a postfix expression.

    Args:
        expression: A postfix expression

    Returns:
        int: The result of the expression
    """
    stack = []
    operators = {"+", "-", "*", "/", "^"}

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

            elif token == "^":
                stack.append(a**b)

        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack.pop()


# Example usage
postfix_expression = input("Enter a postfix expression: ")
try:
    result = evaluate_postfix(postfix_expression)
    print("Result:", result)
except Exception as e:
    print("Error:", e)
