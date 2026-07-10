import ass18_5_MarvellousNum

def ListPrime(arr):
    sum = 0

    for i in arr:
        if ass18_5_MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum

def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        data.append(no)

    ans = ListPrime(data)

    print("Addition of prime numbers is:", ans)

if __name__ == "__main__":
    main()