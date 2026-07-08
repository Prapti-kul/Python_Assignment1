#Write a lambda 
# function which accepts two numbers and returns addition.

sum = lambda no1,no2: no1 + no2

value1 = int(input("Enter first number: "))

value2 = int(input("Enter second number: "))
print("addition is ",sum(value1,value2))