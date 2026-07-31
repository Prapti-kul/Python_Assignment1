def copyfile(sourcefile,destinationfile):

    fobj1 = open(sourcefile,"r")
    fobj2 = open(destinationfile,"w")

    data = fobj1.read()

    fobj2.write(data)

    fobj1.close()
    fobj2.close()


def main():

    source = input("enter the sourcefile name:")
    destination = input("enter the destinationfile name")

    copyfile(source,destination)

    print(f"content of {source} is copied into the {destination} file successfully")

if __name__ == "__main__":
    main()