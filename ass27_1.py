class Bookstore:
    NoofBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author

        Bookstore.NoofBooks +=1

    def Display(self):
       print(f"{self.Name} by {self.Author}")
       print("No of Books :",Bookstore.NoofBooks)

def main():

    obj1 = Bookstore("Linux system programming","robert Love")
    obj1.Display()

    print()

    obj2 = Bookstore("c programming ","Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()

    
