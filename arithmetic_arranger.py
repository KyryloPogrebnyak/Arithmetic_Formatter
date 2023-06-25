def arithmetic_arranger(problems, display_answer=False):
    if len(problems) > 5:
        return f"Error: Too many problems."

    arranged_problems = []
    top_line = []
    bottom_line = []
    lines = []
    answer = []

    for problem in problems:
        item = problem.split()
        operand1 = item[0]
        operator = item[1]
        operand2 = item[2]
        width = max(len(operand1), len(operand2)) + 2

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        elif not operand1.isdigit() or not operand2.isdigit():
            return f"Error: Numbers must only contain digits."
        elif len(operand1) > 4 or len(operand2) > 4:
            return f"Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))

        top_line.append(operand1.rjust(width))
        bottom_line.append(operator + operand2.rjust(width - 1))
        lines.append("-" * width)
        answer.append(result.rjust(width))

    arranged_problems.append("    ".join(top_line))
    arranged_problems.append("    ".join(bottom_line))
    arranged_problems.append("    ".join(lines))

    if display_answer:
        arranged_problems.append("    ".join(answer))

    return "\n".join(arranged_problems)

