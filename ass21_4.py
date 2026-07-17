#Design a Python application that creates two threads.

# The application should:

# Create two threads.
# Thread 1 should compute the sum of all elements in a given list.
# Thread 2 should compute the product of all elements in the same list.
# After both threads finish execution, return the results to the main thread.
# The main thread should display the sum and product


import threading

numbers = [2,3,4,5]

sum_result =0
product_result =1


def findsum():
    global sum_result
    sum_result = sum(numbers)
    

def findproduct():
    global product_result
    for i in numbers:

        product_result *= i

def main():

    t1 = threading.Thread(target = findsum)

    t2 = threading.Thread(target = findproduct)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("sum =",sum_result)
    print("product =",product_result)


if __name__ == "__main__":
    main()