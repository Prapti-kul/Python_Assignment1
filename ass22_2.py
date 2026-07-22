

# 2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

# Input:

# [10, 15, 20, 25]

# Display:

# Process ID
# Input Number
# Factorial







from multiprocessing import Pool
import os

def fact(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact*i
    return (os.getpid(),no,fact)

def main():

    size = int(input("enter number elements:"))
    numbers =[]

    for i in range(size):
        value = int(input("enter the numbers"))
        numbers.append(value)
    p = Pool()    
    result = p.map(fact,numbers)
    p.close()
    p.join()    
    print("\nProcess ID\tInput Number\tFactorial")

    for pid, num, ans in result:
        print(pid, "\t\t", num, "\t\t", ans)
    

if __name__ =="__main__":
    main()