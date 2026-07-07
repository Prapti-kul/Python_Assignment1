
#Write a program which accepts two numbers and prints addition, 
# subtraction, multiplication and division.

def operation(no1,no2):
    ans1 = no1 +no2
    print("the addition is :",ans1)
    ans2 = no1 - no2
    print("subtraction is :",ans2)
    ans3 = no1 * no2
    print("multiplication is :",ans3)
    ans4 = no1 / no2
    print("division is :",ans4)
  
          



def main():
    value1 = int(input("enter the first number:"))
    value2 = int(input("enter the second number:"))


    operation(value1,value2)



if __name__ == "__main__":
    main()