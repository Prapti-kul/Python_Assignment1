#Q3. Write a program which contains one function 
# named as Add() which accepts two numbers 
# and returns addition of that two numbers.

def Add(no1,no2):
    return no1 + no2
  
    
    


def main():
    value1 =int(input("enter the first number : "))
    value2 =int(input("enter the second number : "))

    Ans = Add(value1,value2)
    print("the addition is",Ans)




if __name__ == "__main__":
    main()    