# Calculator

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

num1 = int(input("What's the first number?: "))

for symbols in operations:
  print(symbols)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

# assign chosen function from dictionary to answer
calculations = operations[operation_symbol]
answer = calculations(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")