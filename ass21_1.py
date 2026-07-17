#Q1. Design a Python application that creates two threads named 
# Prime and NonPrime.
# Requirements
# Both threads should accept a list of integers.
# Prime thread should display all prime numbers from the list.
# NonPrime thread should display all non-prime numbers from the list.



import threading

def chkprime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def Prime(data):
    print("Prime Numbers:")
    for i in data:
        if chkprime(i):
            print(i, end=" ")
    print()


def NonPrime(data):
    print("Non Prime Numbers:")
    for i in data:
        if chkprime(i) == False:
            print(i, end=" ")
    print()


def main():
    data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        data.append(no)

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()