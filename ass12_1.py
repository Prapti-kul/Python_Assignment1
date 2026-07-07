
#Write a program which accepts one character and 
#checks whether it is vowel or consonant.

def check(character):
    if character == 'a' or character == 'e' or character == 'i'or character == 'o'or character == 'u':
        print("the character is vowel")
    else:
        print("character is consonant")    



          



def main():
    value = input("enter the character:")

    check(value)



if __name__ == "__main__":
    main()