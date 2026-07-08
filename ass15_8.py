#Q8. Write a lambda function using filter() which accepts a list of numbers 
# and returns a list of numbers divisible by both 3 and 5.


numbers = [10,20,30,40,50,60,70,80,90,100]
value = list(filter(lambda x: x % 3 ==0 and x % 5 ==0,numbers))
print(value)
