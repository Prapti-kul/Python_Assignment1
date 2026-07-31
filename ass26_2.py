class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        ans = float(input("Radius of circle: "))
        self.Radius = ans

    def CalculateArea(self):
        ans = Circle.PI * self.Radius * self.Radius
        self.Area = ans

    def CalculateCircumference(self):
        ans = 2 * Circle.PI * self.Radius
        self.Circumference = ans

    def Display(self):
        print("Radius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)


def main():
    Obj1 = Circle()
    Obj2 = Circle()

    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()


if __name__ == "__main__":
    main()