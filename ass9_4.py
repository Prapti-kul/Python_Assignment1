#Q3. Write a program which
#  accepts one number and prints the square of that number.


def cube(no1):
   ans = no1 * no1 * no1
   print(f"the cube of {no1} is :",ans)
  
def main():
    value = int(input("enter number :"))
    

    cube(value)





if __name__ == "__main__":
    main()    