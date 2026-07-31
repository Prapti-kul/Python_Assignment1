# Q5) Search a Word in File

# Problem Statement:
# Write a program which accepts a file name and a 
# word from the user and checks whether that word 
# is present in the file or not.



def chkword(filename,word):

    fobj = open(filename,"r")

    data = fobj.read()

    if word in data:
        return True
    else:
        return False


def main():

    name = input("enter the file name : ")
    word = input("enter the word to search :")

    ret = chkword(name,word)

    if ret == True:
        print(word,"is found in",name)
    else:
        print(word,"is not found in",name)

if __name__ == "__main__":
    main()