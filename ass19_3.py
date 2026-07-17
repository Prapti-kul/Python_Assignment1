#Q3. Write a program which contains filter(), map() and reduce() in it.
# Python application contains one list of numbers. List contains 
# the numbers which are accepted from user. Filter should filter out 
# all such numbers which are greater than or equal to 70 and less 
# than or equal to 90. Map function will increase each number by 10. 
# Reduce will return product of all that numbers.


from functools import reduce

filter_x = lambda no : (no >= 70) and (no<=90)
map_x = lambda no : no + 10
reduce_x = lambda x,y: x * y 

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