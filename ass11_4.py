
#Write a program which accepts one 
#number and prints reverse of that number.

def reverse(no):
    rev = 0
    while no > 0:
        digit = no % 10
        rev = rev *10 + digit
        no = no//10

    print("the reverse number is :",rev)    



def main():
    value = int(input("enter the number:"))

    reverse(value)



if __name__ == "__main__":
    main()