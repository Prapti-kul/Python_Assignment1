#Q2. Write a program which contains one function 
#named as ChkNum() which accepts one number.
# If the number is even then display 
# "Even Number" otherwise display "Odd Number".


def ChkNum(no):
    if no % 2==0:
        print("even number")
    else:
        print("odd number")    
    


def main():
    value =int(input("enter the number : "))

    ChkNum(value)
    




if __name__ == "__main__":
    main()    