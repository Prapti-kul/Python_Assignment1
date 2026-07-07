
#Write a program which accepts
# radius of circle and prints area of circle

def circlearea(redius):
    area = 3.14 * redius *redius
    print("the area of the circle is :",area)
   

def main():
    value = int(input("enter redius:"))
   
    circlearea(value)



if __name__ == "__main__":
    main()