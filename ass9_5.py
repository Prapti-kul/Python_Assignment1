#Write a program which accepts one number and checks
#  whether it is divisible by 3 and 5.


def divisible(no1):
    if no1 % 3 ==0 and no1 % 5==0:
        print(f"the number {no1} is divisible by 3 and 5")
    else :
        print(f" {no1} is not divisible by 3 and 5 ")    

  
def main():
    value = int(input("enter number :"))
    

    divisible(value)





if __name__ == "__main__":
    main()    