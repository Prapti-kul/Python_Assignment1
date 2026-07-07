#Write a program which accepts one 
#number and prints factorial of that number.


def factorial(no):
    ans = 1
    for i in range(1, no+1):
        ans = ans * i
    
    print("factorial is :", ans )

  
def main():
    value = int(input("enter number :"))
    

    factorial(value)

if __name__ == "__main__":
    main()    