#Q5. Write a program which contains filter(), map(), and reduce() in it.
#Python application contains one list of numbers. List contains the
#numbers accepted from the user. Filter should filter out all prime 
#numbers. Map function will multiply each prime number by 2.
#Reduce function will return the maximum number from the mapped list.


from functools import reduce


def chkprime(no):
    if no < 2:
        return False
    for i in range(2,no):
        if no % i ==0:
            return False
    return True    
filter_x = lambda no : chkprime(no)
map_x = lambda no : no * 2
reduce_x = lambda x,y: x  if x > y else y

def main():
    data = []

    size = int(input("no of elements:"))
    print("enter elements :")
    for i in range(size):
        no = int(input())
        data.append(no)

    Fdata = list(filter(filter_x,data))
    Mdata = list(map(map_x,Fdata))
    Rdata = reduce(reduce_x,Mdata)

    print("list after filter :",Fdata)
    print("list after map :",Mdata)
    print("after reduce :",Rdata)



if __name__ == "__main__":
    main()