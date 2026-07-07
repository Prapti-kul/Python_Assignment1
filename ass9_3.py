#Q3. Write a program which
#  accepts one number and prints the square of that number.


def square(no1):
   ans = no1 * no1
   print(f"the square of {no1} is :",ans)
  
def main():
    value = int(input("enter number :"))
    

    square(value)





if __name__ == "__main__":
    main()    