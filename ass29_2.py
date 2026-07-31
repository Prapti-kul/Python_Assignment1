


def display(filename):

    fobj = open(filename,"r")
    data = fobj.read()
    print(data)

    fobj.close()



def main():
    name = input("enter file name : ")

    display(name)


if __name__ == "__main__":
    main()