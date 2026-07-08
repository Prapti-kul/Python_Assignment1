#Q7. Write a lambda function which 
#accepts one number and returns True if divisible by 5.

divisible = lambda no: no % 5 == 0

value = int(input("Enter a number: "))
print(divisible(value))