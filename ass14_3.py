#Q3. Write a lambda 
# function which accepts two numbers and returns maximum number.


maximum = lambda no1 ,no2 :  no1 if no1>no2 else no2

value1 = int(input("enter the first number : "))
value2 = int(input("enter the second  number : "))

print("maximum value is is :",maximum(value1,value2))