#Write a program which accepts one number 
#and prints the multiplication table of that number.


def table(no):
    for i in range(1,11):
        print(no * i,end=" ")


  
def main():
    value = int(input("enter number :"))
    

    table(value)





if __name__ == "__main__":
    main()    