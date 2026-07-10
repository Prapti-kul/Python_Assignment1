#Q9. Write a program which accept number 
#from user and return number of digits in that number.


def CountDigits(no):
    count = 0

    while no > 0:
        count = count + 1
        no = no // 10

    return count

def main():
    value = int(input("Enter number: "))
    ans = CountDigits(value)
    print("Number of digits:", ans)

if __name__ == "__main__":
    main()