#Q9. Write a lambda function using reduce() which accepts a list of
#numbers and returns the product of all elements.

from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9]
value = reduce(lambda x,y: x * y,numbers)
print("the product is :",value)
