#Write a program which accepts one 
#number and prints sum of first N natural numbers.


def sum(no):
    ans = 0
    for i in range(1, no+1):
        ans = ans + i
    
    print("sum is :", ans )

  
def main():
    value = int(input("enter number :"))
    

    sum(value)

if __name__ == "__main__":
    main()    