#Q4. Write a program which accept N numbers from user and store it into List. Accept one another 
#number from user and return frequency of that number from List.
def Frequency(arr, value):
    count = 0

    for i in arr:
        if i == value:
            count = count + 1

    return count

def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        data.append(no)

    search = int(input("Enter element to search: "))

    ans = Frequency(data, search)

    print("Frequency is:", ans)

if __name__ == "__main__":
    main()