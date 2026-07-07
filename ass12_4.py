
#Write a program which accepts one number 
#and prints that many numbers starting from 1.

def disaplay(no):
    for i in range(1,no+1):
        print(i,end=" ")

def main():
    value = int(input("enter the first number:"))
    
    disaplay(value)



if __name__ == "__main__":
    main()