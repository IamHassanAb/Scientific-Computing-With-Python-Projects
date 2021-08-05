import re


def arithmetic_arranger(problems, choice=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    top_operands = list()
    bottom_operands = list()
    dashes = ''
    operation = list()
    sol = ''
    solution = ''
    dash = ''
    for problem in problems:
        top_operands.append(problem.split()[0])
        bottom_operands.append(problem.split()[2])
        operation.append(problem.split()[1])
        # Error Handling.
        if re.search('/', problem) or re.search('\*', problem):
            return "Error: Operator must be '+' or '-'."
        if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        for (i, j) in zip(top_operands, bottom_operands):
            if not i.isdigit() or not j.isdigit():
                return 'Error: Numbers must only contain digits.'
        # Formatting
        top = ''
        bottom = ''
        for (i, j, k) in zip(top_operands, bottom_operands, operation):
            length = max(len(i), len(j)) + 2
            if k == '+':
                sol = int(i) + int(j)
            else:
                sol = int(i) - int(j)
            top += i.rjust(length) + '    '
            bottom += k + j.rjust(length - 1) + '    '
        for s in range(length):
            dash += '-'
        dashes += dash + '    '
        dash = ''
        solution += str(sol).rjust(length) + '    '

    if choice is True:
        return top.rstrip() + '\n' + bottom.rstrip() + '\n' \
            + dashes.rstrip() + '\n' + solution.rstrip()
    else:
        return top.rstrip() + '\n' + bottom.rstrip() + '\n' \
            + dashes.rstrip()