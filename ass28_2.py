#Q2) Count Words in a File

# Problem Statement:
# Write a program which accepts a file name from 
# the user and counts the total number of words in
#  that file.

# Input:
# Demo.txt

# Expected Output:
# Total number of words in Demo.txt.




def Countwords(FileName):

    count = 0 
    fobj = open(FileName,"r")

    for line in fobj:
        words = line.split()
        count = count + len(words)

    fobj.close()

    return count

def main():

    name = input("enter the file name :")
    ret = Countwords(name)

    print("the number of words in file is : ",ret)  


if __name__ == "__main__":
    main()