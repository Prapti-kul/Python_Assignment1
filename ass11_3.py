
#Write a program which accepts one number and prints sum of digits.
def sumdigit(no):
    sum = 0
    while no >0:
        digit = no % 10
        sum = sum + digit
        no = no//10

    print("sum of digits is:",sum)    





def main():
    value = int(input("enter the number:"))

    sumdigit(value)



if __name__ == "__main__":
    main()