#Q4. Write a program which contains filter(), map(), and reduce() in it.
#Python application contains one list of numbers. List contains the 
#numbers accepted from the user. Filter should filter out all even 
#numbers. Map function will calculate the square of each filtered number. 
#Reduce function will return the addition of all squared numbers..


from functools import reduce

filter_x = lambda no : no % 2 == 0
map_x = lambda no : no * no
reduce_x = lambda x,y: x + y 

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