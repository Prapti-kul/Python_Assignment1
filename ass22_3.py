# 3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing.Pool.

# Example Input:

# 10000
# 20000
# 30000
# 40000

# Display:

# Total prime count for each number.





from multiprocessing import Pool


def countprime(no):
    prime = 0
    for i in range(1,no+1):
        if no % i == 0:
            prime = prime+1

    if prime == 2:
        return True
    else:
        return False
    
         
def main():
    size = int(input("enter the elements :"))
    numbers = []

    for i in range(size):

        value = int(input("enter the numbers : "))
        numbers.append(value)

    p = Pool()
    
    result = p.map(countprime,numbers)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()