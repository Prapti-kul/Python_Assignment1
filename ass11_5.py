
#Write a program which accepts one number 
#and checks whether it is palindrome or not.

def reverse(no):
    temp = no
    rev = 0
    while no > 0:
        digit = no % 10
        rev = rev *10 + digit
        no = no//10

    if temp == rev:
        print("this number is palindrome")
    else:
        print("this number is not a palindrome")       



def main():
    value = int(input("enter the number:"))

    reverse(value)



if __name__ == "__main__":
    main()