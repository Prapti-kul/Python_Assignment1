#Q5. Write a lambda function which accepts one 
#number and returns True if number is odd otherwise False

Odd = lambda no: no % 2 != 0

value = int(input("Enter a number: "))
print(Odd(value))