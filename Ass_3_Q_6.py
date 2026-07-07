import sys

def display():
    value = input("Enter a value: ")


    print("Data Type:", type(value))
    print("Memory Address:", id(value))
    print("Size in Bytes:", sys.getsizeof(value))

display()