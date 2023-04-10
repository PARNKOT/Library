import math

class Shape:
    def square(self):
        pass
    def message(self):
        print(self.square())

class Triangle(Shape):
    def __init__(self):
        self.a = float(input())
        self.b = float(input())
        self.c = float(input())

    def square(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Rectangle(Shape):
    def __init__(self):
        self.a = float(input())
        self.b = float(input())

    def square(self):
        return self.a * self.b

class Circle(Shape):
    def __init__(self):
        self.r = float(input())
        self.PI = 3.14
        
    def square(self):
        return self.PI * self.r**2

   
if __name__ == '__main__':
    shape = input()
    if shape == 'треугольник':
        triangle = Triangle()
        triangle.message()
    elif shape == 'прямоугольник':
        rectangle = Rectangle()
        rectangle.message()
    elif shape == 'круг':
        circle = Circle()
        circle.message()


#Version2.0
f=input()
S={'треугольник':[3, lambda a, b, c: (((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))**0.5],
   'прямоугольник':[2, lambda a, b: a*b], 
   'круг':[1, lambda a: 3.14*a**2]}
args=[float(input()) for i in range (S[f][0])]
print(S[f][1](*args))