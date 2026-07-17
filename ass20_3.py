#Q3. Design a Python application which creates two 
# threads as EvenList and OddList. Both threads 
# accept a list of integers as a parameter.
#  EvenList adds all even elements from the list, 
# and OddList adds all odd elements from the list.



import threading

def EvenFactor(data):
    sum = 0
    print("even numbers:")
    for i in data:
        if i % 2 == 0:
            print(i,end = " ")
            sum = sum +  i

    print("the sum of Even Elements :",sum)
       

def OddFactor(data):
    sum = 0  
    print("odd numbers:")
    for i in data:
        if i % 2 != 0:
            print(i,end = " ")
            sum = sum +  i

    print("the sum of Odd elements :",sum)

def main():
    data =[]

    size = int(input("enter the number:"))
    print("enter elements:")
    for i in range(size):
        no = int(input())
        data.append(no)

    t1 = threading.Thread(target= EvenFactor,args=(data,))
    t2= threading.Thread(target=OddFactor,args =(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("exit from main")

if __name__ == "__main__":
    main()
