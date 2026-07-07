#Write a program which accepts one number 
#and prints all odd numbers till that number.


def factorial(no):
    ans = 1
    for i in range(1, no+1,3):
        print(i, end=" ")
        
    
   

  
def main():
    value = int(input("enter number :"))

    factorial(value)

if __name__ == "__main__":
    main()    