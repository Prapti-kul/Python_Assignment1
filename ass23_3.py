# Write a program that counts how many even numbers
#  exist between 1 and N using Pool.map().

# Input:

# Data = [1000000, 2000000, 3000000, 4000000]

# Expected Output Format:

# Process ID : 1236
# Input Number : 1000000
# Even Number Count : 500000



from multiprocessing import Pool
import os

def counteven(no):
    count = 0
    for i in range(2,no+1,2):
        count = count + 1
    return (os.getpid(),no,count)

def main():

    size = int(input("enter number elements:"))
    numbers =[]

    for i in range(size):
        value = int(input("enter the numbers"))
        numbers.append(value)
    p = Pool()    
    result = p.map(counteven,numbers)
    p.close()
    p.join()    
    print("\nProcess ID\tInput Number\teven number count")

    for pid, num, ans in result:
        print(pid, "\t\t", num, "\t\t", ans)
    

if __name__ =="__main__":
    main()