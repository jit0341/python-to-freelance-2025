
def add(a,b):
  return a + b
def subtract(a,b):
  return a - b
def multiply(a,b):
  return a * b
def divide(a,b):
  if b == 0:
    return "Error: can not divide by zero!"
  return a / b



while True:
  a = int(input("Enter first number:"))
  b = int(input("Enter second number:"))
  operation = input("Enter operation(+, -, *, /): ")
  if operation == "+":
        result = add(a,b)
        print(f"Result: {result}")

  elif operation == "-":
        result = subtract(a,b)
        print(f"Result: {result}")

  elif operation == "*":
        result = multiply(a,b)
        print(f"Result: {result}")

  elif operation == "/":
        result = divide(a,b)
        print(f"Result: {result}")

  else:
        print("Invalid operations!")

  continue_cal = input("Do another calculation? (yes/no):")
  if continue_cal == "no":
         break
