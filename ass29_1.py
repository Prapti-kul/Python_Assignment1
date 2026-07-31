#Q1) Check File Exists in Current Directory
import os

def chkfile(filename):

    if os.path.exists(filename):
        return True
    else:
        return False

def main():
    name = input("enter file name : ")

    ret = chkfile(name)

    if ret == True:
        print(name,"file is exist in directory")

    else:
        print(name,"file does not exits in directory")


if __name__ == "__main__":
    main()