#Q2. Design a Python application that creates two 
# threads named EvenFactor and OddFactor.
# Requirements
# Accept one integer from the user.
# EvenFactor thread:
# Find all even factors.
# Display the sum of even factors.
# OddFactor thread:
# Find all odd factors.
# Display the sum of odd factors.
# After both threads complete, display "Exit from main"



import threading

def EvenFactor(no):
    sum = 0
    print("even numbers:")
    for i in range(1,no +1):
        if no % i ==0:
            if i % 2 == 0:
                print(i,end = " ")
                sum = sum +  i

    print("the sum of Even Factor :",sum)
       

def OddFactor(no):
    sum = 0  
    print("odd numbers:")
    for i in range(1,no +1):
        if no % i ==0:
            if i % 2 != 0:
                print(i,end = " ")
                sum = sum +  i

    print("the sum of Odd Factor :",sum)

def main():
    value = int(input("enter the number:"))

    t1 = threading.Thread(target= EvenFactor,args=(value,))
    t2= threading.Thread(target=OddFactor,args =(value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("exit from main")

if __name__ == "__main__":
    main()
