#Q7. Write a lambda function using filter() which accepts a list of strings and 
# returns a list of strings having length greater than 5.


numbers = ["prapti","anjali","ram","kulkarni","sham","sanskruti"]
value = list(filter(lambda x: len(x) > 5,numbers))
print(value)
