#Q2. Write a program which contains one lambda function which 
#accepts two parameters and returns its multiplication.


mul = lambda No1,No2 : No1 * No2

value1 = int(input("enter the first number : "))
value2 = int(input("enter the second number : "))

print("the numtiplication is : ",mul(value1,value2))