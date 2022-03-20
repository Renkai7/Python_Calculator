# Calculator
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Operation Dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Recursion
def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  # list operation symbols
  for symbols in operations:
    print(symbols)
    
  continue_calculation = True
  while continue_calculation:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    # assign chosen function from dictionary to answer
    calculations = operations[operation_symbol]
    answer = round(calculations(num1, num2), 2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating {answer}, or type 'n' to start a new calculation: ").lower() == 'y':
      num1 = answer
    else:
      continue_calculation = False
      calculator()
          
calculator()
    
  