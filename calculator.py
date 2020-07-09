"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def main():
    while True:
        input_string = input("Enter equation: ")
        tokens = input_string.split()
        if tokens[0] == "q":
            break
        operator, *nums = tokens
        try:
            num_floats = []
            for num in nums:
                num_floats.append(float(num))
        except:
            print("Your operands are not valid. Please enter numbers.")
            continue
        if operator == "+":
            answer = add(num_floats[0], num_floats[1])
        elif operator == "-":
            answer = subtract(num_floats[0], num_floats[1])
        elif operator == "*":
            answer = multiply(num_floats[0], num_floats[1])
        elif operator == "/":
            answer = divide(num_floats[0], num_floats[1])
        elif operator == "square":
            answer = square(num_floats[0])
        elif operator == "cube":
            answer = cube(num_floats[0])
        elif operator == "pow":
            answer = power(num_floats[0], num_floats[1])
        elif operator == "mod":
            answer = mod(num_floats[0], num_floats[1])
        else: #If operator doesn't match any of the above, then it's invalid.
            print("That's not a valid operator. Try again.")
            continue
        print(answer)

main()
