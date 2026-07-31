# Q1) Count Lines in a File
# Problem Statement

# Write a program that accepts a file name from the user and counts how many lines are present in that file.

# Algorithm
# Accept the file name from the user.
# Open the file in read mode.
# Initialize a counter to 0.
# Read the file line by line.
# Increment the counter for every line.
# Display the total number of lines.
# Close the file.


def CountLines(FileName):
    Count = 0

    fobj = open(FileName, "r")

    for line in fobj:
        Count = Count + 1

    fobj.close()

    return Count


def main():
    Name = input("Enter file name : ")

    Ret = CountLines(Name)

    print("Total number of lines :", Ret)


if __name__ == "__main__":
    main()