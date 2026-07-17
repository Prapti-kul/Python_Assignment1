#Q5. Design a Python application that creates two threads named 
# Thread1 and Thread2.
# Requirements
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Thread2 should start only after Thread1 has completed.


import threading

def Thread1():
    
    print("the numbers in Thread 1:")
    for i in range(1,51):
        print(i,end = " ")
    print()    
                

       

def Thread2():
    print("the numbers in Thread 2:")
    for i in range(50,0,-1):
        print(i,end = " ")
    print() 

def main():


    t1 = threading.Thread(target= Thread1)
    t2= threading.Thread(target=Thread2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("exit from main")

if __name__ == "__main__":
    main()
