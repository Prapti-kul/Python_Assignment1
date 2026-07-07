#Write a program which accepts one number 
#and checks whether it is prime or not.


def count(no):
    count=0

    while no > 0:
        count = count + 1
        no = no // 10

    print("count of digits is:",count)




def main():
    value = int(input("enter number : "))

    count(value)




if __name__ == "__main__":
    main()    