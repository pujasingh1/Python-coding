#Calculator

#Add 
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Division
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

number1 = int(input("What's the first number?: "))
for symbols in operations:
  print(symbols)
pick_symbols = (input("Pick an operation: "))
number2 = int(input("What's the next number?: "))
calculation_function = operations[pick_symbols]
answer = calculation_function(number1, number2)

print(f"{number1} {pick_symbols} {number2} = {answer}")
