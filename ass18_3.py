# Q3. Write a program which accept N numbers from user 
# and store it into List. Return Minimum number from that List.

def Minimum(arr):
    min = arr[0]

    for i in arr:
        if i < min:
            min = i

    return min

def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        data.append(no)

    ans = Minimum(data)

    print("Minimum number is:", ans)

if __name__ == "__main__":
    main()