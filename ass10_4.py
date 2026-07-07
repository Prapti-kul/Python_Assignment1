#Write a program which accepts one number 
#and prints all even numbers till that number.


def factorial(no):
    ans = 1
    for i in range(2, no+1,2):
        print(i, end=" ")
        
    
   

  
def main():
    value = int(input("enter number :"))

    factorial(value)

if __name__ == "__main__":
    main()    