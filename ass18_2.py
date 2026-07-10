# Q2. Write a program which accept N numbers from user 
# and store it into List. Return Maximum number from that List.

def Max(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i 
    return max   

def main():
    value= int(input("enter the number of elements :"))
    data=[]
    print("enter the elements :")
    for i in range(value):
        no = int(input())
        data.append(no)
    
    ans = Max(data)
    print("the maximum number is :",ans)

    


if __name__ == "__main__":
    main()