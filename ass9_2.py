
#Q2. Write a program which contains one 
# function ChkGreater() that accepts two numbers and prints the greater number.


def ChkGreater(no1,no2):
    if no1 > no2:
        print(f"the grater number is {no1}")

    else:
        print(f"the greater number is {no2}")
  
def main():
    value1 = int(input("enter first number :"))
    value2 = int(input("enter second number :"))

    ChkGreater(value1,value2)





if __name__ == "__main__":
    main()    