#Q7. Write a program which contains one 
# function that accepts one number from the user 
# and returns True if the number 
# is divisible by 5, otherwise returns False.



def Check(no):
    if no % 5==0:
        return True      
    else:
        return False


def main():
    value = int(input("enter the number : "))
    result = Check(value)
    print(result)




if __name__ == "__main__":
    main()