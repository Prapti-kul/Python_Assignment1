class Numbers:


    def __init__(self,Value):
        self.Value = Value

    def Chkprime(self):

        if self.Value <=1:
            return False

        for i in range(2,self.Value):
            if self.Value % i ==0:
                return False

        return True

    def Chkperfect(self):

        sum = 0 

        for i in range(1,self.Value):
            if self.Value % i ==0:
                sum = sum +i

        if sum == self.Value:
            return True
        else:
            return False


    def Factors(self):
        print("factors are :",end =" ")

        for i in range(1,self.Value +1):
            if self.Value % i == 0:
                print(i,end = " ")
        print()

    def SumFactors(self):
        sum = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum = sum + i  

        return sum

def main():
    no1 = int(input("enter the first number :"))
    obj1 = Numbers(no1)

    print("prime:",obj1.Chkprime())
    print("perfect :",obj1.Chkperfect())
    obj1.Factors()
    print("sum of factors are:",obj1.SumFactors())

    print("--------------------------------------------------------------")

    no2 = int(input("enter the first number :"))
    obj2 = Numbers(no2)
        
    print("prime:",obj2.Chkprime())
    print("perfect :",obj2.Chkperfect())
    obj2.Factors()
    print("sum of factors are:",obj2.SumFactors())
    
if __name__ == "__main__":
    main()


        