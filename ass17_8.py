#8. Pattern Program

# Input: 5

# Output:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def display(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()    





def main():
    value = int(input("enter the number : "))
    display(value)
                



if __name__ == "__main__":
    main()