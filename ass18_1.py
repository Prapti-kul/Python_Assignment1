# Q1. Write a program which accept N numbers from user and store it into List.
# Return addition of all elements from that List.

def Add(arr):
    sum = 0 
    for i in arr:
        sum = sum + i

    return sum    

def main():
    value= int(input("enter the number of elements :"))
    data=[]
    print("enter the elements :")
    for i in range(value):
        no = int(input())
        data.append(no)
    
    ans = Add(data)
    print("the addition of elements is :",ans)

    


if __name__ == "__main__":
    main()