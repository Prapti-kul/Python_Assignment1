#Q1. Design a Python application that 
#creates two separate threads named Even and Odd.
# Requirements
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.



import threading

def Even():
    print("even numbers:")
    for i in range(2,21,2):
        print(i,end = " ")

def Odd():
    print("odd numbers:")
    for i in range(1,20,2):
        print(i,end = " ")


def main():

    t1 = threading.Thread(target= Even)
    t2= threading.Thread(target=Odd )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("exit from main")



if __name__ == "__main__":
    main()
