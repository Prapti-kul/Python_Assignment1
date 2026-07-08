#Q10. Write a lambda function using filter() which accepts 
#a list of numbers and returns the count of even numbers.


numbers = [1,2,3,4,5,6,7,8,9.10]
value = len(list(filter(lambda x: x % 2==0,numbers)))
print(value)
