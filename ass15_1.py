#Q1. Write a lambda function using map() which accepts 
#a list of numbers and returns a list of squares of each number.


numbers = [2,4,8,9]
value = list(map(lambda x: x*x,numbers))
print(value)
