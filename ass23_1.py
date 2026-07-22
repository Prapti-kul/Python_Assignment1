# Q1

# Write a Python program using multiprocessing.Pool to calculate 
# the sum of all even numbers from 1 to N for 
# every number from the given list.

# Input:

# Data = [1000000, 2000000, 3000000, 4000000]

# Expected Task:

# For each number N, calculate:

# 2 + 4 + 6 + ... + N

# Display:

# Process ID
# Input Number
# Sum of Even Numbers

from multiprocessing import Pool
import os

def sumeven(no):
    total = 0
    for i in range(2,no+1,2):
        total = total + i
    return (os.getpid(),no,total)

def main():

    size = int(input("enter number elements:"))
    numbers =[]

    for i in range(size):
        value = int(input("enter the numbers"))
        numbers.append(value)
    p = Pool()    
    result = p.map(sumeven,numbers)
    p.close()
    p.join()    
    print("\nProcess ID\tInput Number\tsum of even number")

    for pid, num, ans in result:
        print(pid, "\t\t", num, "\t\t", ans)
    

if __name__ =="__main__":
    main()