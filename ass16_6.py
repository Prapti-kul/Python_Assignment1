#Q6. Write a program which accepts a number 
# from the user and checks whether that number 
# is positive, negative or zero.




def Check(no):
    if no == 0:
        print("the number is zero ")
    elif no < 0:
        print("the number is negative")
    else :
        print("the number is positive")        


def main():
    value = int(input("enter the number : "))
    Check(value)




if __name__ == "__main__":
    main()