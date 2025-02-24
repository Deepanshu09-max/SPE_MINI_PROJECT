#!/usr/bin/env python3
import math

def square_root(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return "Invalid input for square root."

def factorial(x):
    try:
        return math.factorial(int(x))
    except (ValueError, OverflowError):
        return "Invalid input for factorial."

def natural_log(x):
    try:
        return math.log(x)
    except ValueError:
        return "Invalid input for natural logarithm."

def power(x, b):
    try:
        return math.pow(x, b)
    except Exception as e:
        return f"Error computing power: {e}"

def menu():
    print("Scientific Calculator")
    print("1. Square Root (√x)")
    print("2. Factorial (!x)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            x = float(input("Enter a number: "))
            print("Result:", square_root(x))
        elif choice == '2':
            x = int(input("Enter an integer: "))
            print("Result:", factorial(x))
        elif choice == '3':
            x = float(input("Enter a number: "))
            print("Result:", natural_log(x))
        elif choice == '4':
            x = float(input("Enter base value: "))
            b = float(input("Enter exponent: "))
            print("Result:", power(x, b))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
