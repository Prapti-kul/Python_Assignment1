#Q4. Return addition of factors
def prime(no):
    count = 0
    for i in range(1,no+1):
        if no % i ==0:
            count = count + 1
        
    if count == 2:
        return True
    else:
        return False
    

def main():
    value = int(input("enter the number : "))
    if prime(value):
        print("it is prime number")
    else:    
        print("it is not a prime number")

if __name__ ==  "__main__":
    main()