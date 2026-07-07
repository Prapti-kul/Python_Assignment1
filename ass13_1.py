
#Write a program which accepts length 
#and width of rectangle and prints area.
def rectarea(len,width):
    area = len * width
    print("the area of the rectangle :",area)
   

def main():
    value1 = int(input("enter length:"))
    value2= int(input("enter width:"))
    
    rectarea(value1,value2)



if __name__ == "__main__":
    main()