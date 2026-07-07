
#Write a program which accepts one 
#number and prints binary equivalent.

def binary(no):
    ans = bin(no)
    print(f"binary number of {no} is {ans}")

def main():
    value = int(input("Enter a number: "))

    binary(value)

if __name__ == "__main__":
    main()