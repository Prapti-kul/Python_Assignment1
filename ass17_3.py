#Q3. Return factorial
def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i

    return fact

def main():
    value = int(input("enter the number : "))
    ans = factorial(value)
    print("factorial is : ",ans)

if __name__ ==  "__main__":
    main()