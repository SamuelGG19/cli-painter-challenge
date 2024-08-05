# TODO: Add code here
import matplotlib.pyplot as plt
import numpy as np


class Point:

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Circle:

    def __init__(self, radius: float):
        self.radius: float = radius
        self.center.point: list[Point] = []

    def area(self, radius: float) -> float:
        return np.pi * radius ** 2

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self, x: point, y: point, r: float) -> str | tuple | float:
        center = Point(x, y)
        self.r: float = r
        return "Circle with center at", center, "and radius", r

class Triangle:

    def __init__(self):
        self.point_1.point: list[Point] = []
        self.point_2.point: list[Point] = []
        self.point_2.point: list[Point] = []

    def area(self, base: float, height: float) -> float:
        return base * times / 2

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def __str__(self, x1: point, y1: point, x2: point, y2: point, x3: point, y3: point) -> str:
        v1 = Point(x1, y1)
        v2 = Point(x2, y2)
        v3 = Point(x3, y3)
        return