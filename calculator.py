"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def main():
    while True:
        input_string = input()
        tokens = input_string.split()
        if tokens[0] == "q":
            break
        operator, *nums = tokens
        if operator == "+":
            answer = add(float(tokens[1]), float(tokens[2]))
        elif operator == "-":
            answer = subtract(float(tokens[1]), float(tokens[2]))
            print(answer)
        elif operator == "*":
            answer = multiply(float(tokens[1]), float(tokens[2]))
            print(answer)
        elif operator == "/":
            answer = divide(float(tokens[1]), float(tokens[2]))
            print(answer)
        elif operator == "square":
            answer = square(float(tokens[1]))
            print(answer)
        elif operator == "cube":
            answer = cube(float(tokens[1]))
            print(answer)
        elif operator == "pow":
            answer = power(float(tokens[1]), float(tokens[2]))
            print(answer)
        elif operator == "mod":
            answer = mod(float(tokens[1]), float(tokens[2]))
            print(answer)
        else:
            print("That's not a valid operator. Try again.")
            continue
        print(answer)

main()

# Replace this with your code
