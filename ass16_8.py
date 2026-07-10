#Q8. Write a program which accepts a number from
#  the user 
# and prints that many * on the screen.



def Check(no):
    for i in range(no):
        print("*",end=" ")
   

def main():
    value = int(input("enter the number : "))
    Check(value)
  



if __name__ == "__main__":
    
    main()