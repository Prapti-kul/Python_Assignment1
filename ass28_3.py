# Q3 — Display File Line by Line

# The program takes a file name and displays every
#  line from that file.


def Displayfile(FileName):

     
    fobj = open(FileName,"r")

    for line in fobj:
        print(line,end=" ")

    fobj.close()

def main():

    name = input("enter the file name :")
    Displayfile(name)

if __name__ == "__main__":
    main()