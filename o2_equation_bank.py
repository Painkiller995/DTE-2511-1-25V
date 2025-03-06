"""
This module solves the equation bank task.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import os
import random

RANDOM_RANGE = -9, 9
NUMBER_OF_EQUATIONS = 4


def generate_equation() -> tuple[str, int]:
    """
    Generates a random linear equation of the form ax + b = cx + d.
    The equation is guaranteed to have a whole number solution.

    Returns:
        tuple: A tuple containing the equation string and the solution.
    """
    while True:
        start_range, end_range = RANDOM_RANGE
        a = random.randint(start_range, end_range)
        b = random.randint(start_range, end_range)
        c = random.randint(start_range, end_range)

        if a == c:
            continue  # Skip invalid equations where a == c

        # Ensure (d - b) is divisible by (a - c) to get a whole number solution
        d = b + (a - c) * random.randint(start_range, end_range)

        equation = f"{format_coefficient(a)}x {format_constant(b)} = {format_coefficient(c)}x {format_constant(d)}"
        solution = (d - b) // (a - c)
        return equation, solution


def format_coefficient(coef: int) -> str:
    """
    Formats the coefficient of a term in a linear equation.

    Args:
        coef: The coefficient to format.

    Returns:
        str: The formatted coefficient.
    """
    if coef == 1:
        return ""
    elif coef == -1:
        return "-"
    else:
        return str(coef)


def format_constant(const: int) -> str:
    """
    Formats the constant of a term in a linear equation.

    Args:
        const: The constant to format.

    Returns:
        str: The formatted constant.
    """
    if const > 0:
        return f"+ {const}"
    elif const < 0:
        return f"- {-const}"
    else:
        return ""


def generate_equations_for_students(student_names: list[str]) -> dict[str, dict[str, list[str] | list[int]]]:
    """
    Generates a set of linear equations for each student in the list.

    Args:
        student_names: A list of student names.

    Returns:
        dict: A dictionary containing the student names as keys and a dictionary of equations, solutions, and answers as values.
    """
    student_equations: dict[str, dict[str, list[str] | list[int]]] = {}

    for student_name in student_names:
        equations: list[str] = []
        solutions: list[int] = []
        student_answers: list[int] = []
        for _ in range(NUMBER_OF_EQUATIONS):
            equation, solution = generate_equation()
            equations.append(equation)
            solutions.append(solution)

        student_equations[student_name] = {
            "equations": equations,
            "solutions": solutions,
            "answers": student_answers,
        }

    return student_equations


def clear_screen() -> None:
    """
    Clears the screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def view_result(student_name: str, student_data: dict[str, list[str] | list[int]]) -> None:
    """
    View the result of the student session including the correct answers and the student's answers.

    Args:
        student_name: The name of the student.
        student_data: A dictionary containing the student data.
    """
    clear_screen()
    print(f"Thank you {student_name} for participating in the session!\n")
    print("Here are your results:\n")

    number_of_correct_answers = 0

    equations = student_data["equations"]
    solutions = student_data["solutions"]
    answers = student_data["answers"]

    for i, _ in enumerate(equations):
        equation = equations[i]
        solution = solutions[i]
        answer = answers[i]

        print(f"Equation {i + 1}: {equation}")
        print(f"Correct answer: {solution}")
        print(f"Your answer: {answer}")

        if answer == solution:
            print("Correct!\n")
            number_of_correct_answers += 1
        else:
            print("Incorrect!\n")

    print(f"Total correct answers: {number_of_correct_answers} out of {NUMBER_OF_EQUATIONS}\n")


def student_session(student_equations: dict[str, dict[str, list[str] | list[int]]]) -> None:
    """
    Simulates a student session where the student solves the equations.

    Args:
        student_equations: A dictionary containing the student names as keys and a dictionary as values.
    """
    clear_screen()
    print("Welcome to the Student Session!\n")

    while True:
        student_name = input("Enter student name: ").strip()

        clear_screen()
        print("\nWelcome!\n")

        if student_name not in student_equations:
            print("Invalid student name. Please try again.\n\n")
            continue

        student_data = student_equations[student_name]

        equations = student_data["equations"]
        solutions = student_data["solutions"]
        answers: list[int] = []

        if not equations or not solutions:
            print("No equations found for this student.")
            break

        print(f"Hello {student_name}! Let's solve some equations.\n")
        print(f"You will be presented with {NUMBER_OF_EQUATIONS} equations.\n")

        input("Press Enter to start the session...")

        for equation in equations:
            clear_screen()
            print(f"\nSolve the equation: {equation}")

            while True:
                answer = input("Enter your answer: ").strip()

                if not answer.isdigit():
                    print("Invalid input. Please enter a number.")
                    continue

                student_answer = int(answer)
                answers.append(student_answer)
                break

        student_data["answers"] = answers
        student_equations[student_name] = student_data
        view_result(student_name, student_data)


if __name__ == "__main__":
    students = ["John", "Maria", "Fredrick", "Sara", "Julia"]
    generated_eq = generate_equations_for_students(students)
    student_session(generated_eq)
