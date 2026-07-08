#Q10. Write a lambda function which 
#accepts three numbers and returns largest number.


larger = lambda a, b, c: a if a > b and a > c else (b if b > c else c)

value1 = int(input("Enter first number: "))

value2 = int(input("Enter second number: "))

value3 = int(input("Enter third number: "))
print("multiplication is ",larger(value1,value2,value3))