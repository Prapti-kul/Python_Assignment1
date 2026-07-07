
#Write a program which accepts one number and 
#prints that many numbers in reverse order.

def reverse(no):
    for i in range(no,0,-1):
        print(i,end=" ")

def main():
    value = int(input("enter the first number:"))
    
    reverse(value)



if __name__ == "__main__":
    main()