#Q3. Design a Python application which creates two 
# threads as EvenList and OddList. Both threads 
# accept a list of integers as a parameter.
#  EvenList adds all even elements from the list, 
# and OddList adds all odd elements from the list.



import threading

def Small(str):
    count = 0
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in str:
        if ch.islower():
            count = count + 1

    print("Small letters:", count)


def Capital(str):
    count = 0
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in str:
        if ch.isupper():
            count = count + 1

    print("Capital letters:", count)


def Digits(str):
    count = 0
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in str:
        if ch.isdigit():
            count = count + 1

    print("Digits:", count)


def main():

    value = input("Enter the string: ")

    t1 = threading.Thread(target=Small, args=(value,), name="Small")
    t2 = threading.Thread(target=Capital, args=(value,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(value,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()