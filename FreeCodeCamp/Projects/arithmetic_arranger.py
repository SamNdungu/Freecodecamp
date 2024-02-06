def arithmetic_arranger(problems, show_solution=False):
  # Check if there are more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."
  
  arranged_problems = ""
  top_line = ""
  bottom_line = ""
  separator_line = ""
  result_line = ""
  
  for problem in problems:
    num1, operator, num2 = problem.split()
  
    if not (operator == '+' or operator == '-'):
      return "Error: Operator must be '+' or '-'."
  
    if not (num1.isdigit() and num2.isdigit()):
      return "Error: Numbers must only contain digits."
  
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
  
    width = max(len(num1), len(num2)) + 2
    top_line += num1.rjust(width) + '    '
    bottom_line += operator + num2.rjust(width - 1) + '    '
    separator_line += '-' * width + '    '
  
    if show_solution:
      result = str(eval(problem))
      result_line += result.rjust(width) + '    '
  
  arranged_problems += top_line.rstrip() + '\n' + bottom_line.rstrip(
  ) + '\n' + separator_line.rstrip()
  
  if show_solution:
    arranged_problems += '\n' + result_line.rstrip()
  
  return arranged_problems
  
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))  