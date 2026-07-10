#Q4. Return addition of factors
def Addfact(no):
    sum = 0
    for i in range(1,no):
        if no % i ==0:
            sum = sum + i
        

    return sum

def main():
    value = int(input("enter the number : "))
    ans = Addfact(value)
    print("factorial is : ",ans)

if __name__ ==  "__main__":
    main()