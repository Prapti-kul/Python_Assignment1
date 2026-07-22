# Q2

# Write a Python program using multiprocessing.Pool 
# to
# calculate the sum of all odd numbers from 1 to N.

# Input:

# Data = [1000000, 2000000, 3000000, 4000000]

# Expected Task:

# For each number N, calculate:

# 1 + 3 + 5 + ... + N

# Expected Output Format:

# Process ID : 1235
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000



from multiprocessing import Pool
import os

def sumodd(no):
    total = 0
    for i in range(1,no+1,2):
        total = total + i
    return (os.getpid(),no,total)

def main():

    size = int(input("enter number elements:"))
    numbers =[]

    for i in range(size):
        value = int(input("enter the numbers"))
        numbers.append(value)
    p = Pool()    
    result = p.map(sumodd,numbers)
    p.close()
    p.join()    
    print("\nProcess ID\tInput Number\tsum of odd number")

    for pid, num, ans in result:
        print(pid, "\t\t", num, "\t\t", ans)
    

if __name__ =="__main__":
    main()