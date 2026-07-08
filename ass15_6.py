#Q6. Write a lambda function using reduce() which accepts a 
# list of numbers and returns the minimum element.


from functools import reduce
numbers = [1,5,10,45,3,4,5]
value = reduce(lambda x,y: x if x<y else y,numbers)
print(value)
