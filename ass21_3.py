#Design a Python application where multiple threads update a shared variable.

# The application should:

# Create multiple threads (two or more).
# Use a shared variable (for example, counter) that all threads can access.
# Each thread should increment the shared variable multiple times.
# Use a Lock to ensure that only one thread updates the shared variable at a time, avoiding race conditions.
# After all threads complete their execution, the main thread should display the final value of the shared variable.


import threading
counter = 0
lock = threading.Lock()

def increment(no):
    global counter
    
    for i in range(no):
        lock.acquire()
        counter += 1 
        lock.release()

def main():
    value = int(input("enter the number:"))
 
    t1 = threading.Thread(target = increment,args = (value,))

    t2 = threading.Thread(target = increment,args = (value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final counter :",counter)


if __name__ == "__main__":
    main()