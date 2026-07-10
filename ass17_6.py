#6. Pattern Program
#Input: 5
#Output:
# * * * * *
# * * * *
# * * *
# * *
# *

def display(no):
    for i in range(no,0,-1):
        for j in range(i):
            print("*",end=" ")
        print(i)    

def main():
    value = int(input("enter the number : "))
    display(value)

if __name__ == "__main__":
    main()