
#Q2. Pattern
def display(no):
    for i in range(no):
        for j in range(no):
            print("*", end = " ")
        print()    

        




def main():
    value= int(input("enter the number : "))
    display(value)


if __name__ == "__main__":
    main()