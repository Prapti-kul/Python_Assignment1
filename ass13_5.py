
#Write a program which 
#accepts marks and displays grade.

def display(marks):
    if marks >= 90:
        print("A Grade")
    elif marks >= 80:
        print("B Grade")
    elif marks >= 70:
        print("c grade")
    else:
        print("pass")       

def main():
    value = int(input("Enter a number: "))

    display(value)

if __name__ == "__main__":
    main()