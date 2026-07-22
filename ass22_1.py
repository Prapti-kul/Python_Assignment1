# 1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

# Example Input:

# [1000000, 2000000, 3000000, 4000000]

# Expected Output:

# [
# 333333833333500000,
# 2666668666667000000,
# ...
# ]



from multiprocessing import Pool

def sumsquare(no):
    total =0

    for i in range(1,no+1):
        total = total + (i*i)

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