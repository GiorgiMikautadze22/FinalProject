import math
from math import hypot


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
       return self.__x

    def gety(self):
       return self.__y

    def distance_from_xy(self, x, y):
        A = abs(self.__x - x)
        B = abs(self.__y - y)
        return hypot(A,B)

    def distance_from_point(self, point):
        A = abs(self.__x - point.getx())
        B = abs(self.__y - point.gety())
        return hypot(A, B)


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
