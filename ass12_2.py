
#Write a program which accepts 
# one number and prints its factors.

def factor(no):
    for i in range (1 ,no+1):
        if no % i == 0:
            print(i,end=" ")

          



def main():
    value = int(input("enter the number:"))

    factor(value)



if __name__ == "__main__":
    main()