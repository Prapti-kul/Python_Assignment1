#Write a program which accepts one number 
#and checks whether it is prime or not.


def chkprime(no):
    count=0

    for i in range(1,no+1):
        if no % i == 0:
            count = count + 1 
    

    if count == 2:
        print("prime number")
    else:
        print("not prime number")




def main():
    value = int(input("enter number : "))

    chkprime(value)




if __name__ == "__main__":
    main()    