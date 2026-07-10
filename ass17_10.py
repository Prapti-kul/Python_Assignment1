#Q10. Write a program which accept number from 
# user and return addition of digits in that number.



def AddDigits(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum

def main():
    value = int(input("Enter number: "))
    ans = AddDigits(value)
    print("Addition of digits:", ans)

if __name__ == "__main__":
    main()