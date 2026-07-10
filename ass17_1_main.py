#Q1. Create a module named Arithmetic with 
# Add(), Sub(), Mult(), Div()

import ass17_1_Arithmetic

def main():
    value1 = int(input("enter the first number : "))
    value2 = int(input("enter the second number : "))

    print("addition is",ass17_1_Arithmetic.Add(value1,value2))
    print("subtraction is",ass17_1_Arithmetic.Sub(value1,value2))
    print("multiplication is",ass17_1_Arithmetic.Mult(value1,value2))
    print("division is",ass17_1_Arithmetic.Div(value1,value2))


if __name__ == "__main__":
    main()