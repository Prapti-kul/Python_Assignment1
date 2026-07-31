# Q4) Compare Two Files (Command Line)
# Problem Statement:

# Write a program which accepts two file names through command line arguments and compares the contents of both files.

# If both files contain the same contents, display Success.
# Otherwise, display Failure.

import sys

def CompareFiles(FileName1, FileName2):

    fobj1 = open(FileName1, "r")
    fobj2 = open(FileName2, "r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if Data1 == Data2:
        return True
    else:
        return False


def main():

    if len(sys.argv) == 3:

        Ret = CompareFiles(sys.argv[1], sys.argv[2])

        if Ret == True:
            print("Success")
        else:
            print("Failure")

    else:
        print("Invalid number of arguments")


if __name__ == "__main__":
    main()