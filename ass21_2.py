#Q1. Design a Python application that creates two threads named 
# Prime and NonPrime.
# Requirements
# Both threads should accept a list of integers.
# Prime thread should display all prime numbers from the list.
# NonPrime thread should display all non-prime numbers from the list.



import threading

def maximum(data):
    max = data[0]
    for i in data:
        if i > max:
            max = i
    print("maximum element is :",max)         

def minimum(data):
    min = data[0]
    for i in data:
        if i < min:
            max = i
    print("minimum element is :",min)        

def main():
    data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        data.append(no)

    t1 = threading.Thread(target=maximum, args=(data,))
    t2 = threading.Thread(target=minimum, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()