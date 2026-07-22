# 4. Write a program that calculates:
# 1^5 + 2^5 + 3^5 + ..... + N^5

# for multiple values of N simultaneously using Pool.

# Input:

# [
# 1000000,
# 2000000,
# 3000000,
# 4000000
# ]

# Display:

# Measure total execution time.


from multiprocessing import Pool

def sumsquare(no):
    total =0

    for i in range(1,no+1):
        total = total + (i**5)

    return total

def main():
    size = int(input("enter the elements:"))

    numbers = []
    for i in range(size):
        value = int(input("Enter the number:"))
        numbers.append(value)

    p= Pool()


    result = p.map(sumsquare,numbers)    
    
    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()