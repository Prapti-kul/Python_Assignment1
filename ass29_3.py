# Q3) Copy File Contents into a New File (Command 
# Line)
# Problem Statement:

# Write a program which accepts an existing file
#  name through command line arguments, creates a 
# new file named Demo.txt, and copies all contents
#  from the given file into Demo.txt.

import sys

def copyfile(filename):

    fobj1 = open(filename,"r")
    fobj2 = open("Demo.txt","w")


    data = fobj1.read()

    fobj2.write(data)

    fobj1.close()
    fobj2.close()

def main():
    if len(sys.argv) == 2:
        copyfile(sys.argv[1])
        print("content copied successfully into Demo.txt")

    else:
        print("invalid number of argunments")

if __name__ == "__main__":
    main()