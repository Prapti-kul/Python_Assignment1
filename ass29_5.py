# Q5) Frequency of a String in File
# Problem Statement:

# Write a program which accepts a file name and 
# one string from the user and returns the frequency 
# (number of occurrences) of that string in the file.

def CountFrequency(FileName, Word):

    fobj = open(FileName, "r")

    Data = fobj.read()

    fobj.close()

    Count = Data.count(Word)

    return Count


def main():

    Name = input("Enter file name : ")
    Word = input("Enter string : ")

    Ret = CountFrequency(Name, Word)

    print("Frequency of", Word, "is :", Ret)


if __name__ == "__main__":
    main()