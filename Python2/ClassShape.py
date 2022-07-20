import math

class Polygon2D:
    def __init__(self) -> None:
        pass

    def perimeter2d(self, base:int, height:int) -> int:
        return 2*base + 2*height

    def area(self, base:int, height:int) -> int:
        return base*height

    def circumference(self, radius:int) -> float:
        return 2*math.pi*radius

class Polygon3D:
    def __init__(self) -> None:
        pass

    def perimeter3d():
        pass

    def volume(self, base:int, height:int, width:int) -> int:
        return base*height*width

    def surface_area(self):
        pass

class Rectangle(Polygon2D, Polygon3D):
    pass

class RightTri(Polygon2D, Polygon3D):
    pass

class Circle(Polygon2D, Polygon3D):
    pass

def main():

    rec = Rectangle()

    rTri = RightTri()

    cir = Circle()

if __name__ == "__main__":
    main()
