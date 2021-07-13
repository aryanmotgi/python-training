import math

class Triangle:
    def __init__(self, side_1, side_2, side_3, center=(0.0, 0.0)):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.center = center
    
    def __repr__(self):
        return "Triangle(side_1={s1}, side_2={s2}, side_3={s3} center={c})".format(s1=self.side_1,
                                                                                   s2=self.side_2,
                                                                                   s3=self.side_3,
                                                                                   c=self.center)
    
    def compute_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

class EquilateralTriangle(Triangle):
    def __init__(self, side, center=(0.0, 0.0)):
        super().__init__(side, side, side, center)
    
    def __repr__(self):
        return "EquilateralTriangle(side={s}, center={c})".format(s=self.side1,
                                                                  c=self.center)
    
    def compute_area(self):
        # it doesn't matter which side you use since the triangle is equilateral
        return math.sqrt(3)/2 * (self.side_1 ** 2)/2

t1 = Triangle(2, 3, 4)
print(t1)
print(t1.compute_perimeter())

et1 = EquilateralTriangle(3)
print(et1.compute_area())

import math

class Triangle:
    def __init__(self, side_1, side_2, side_3, center=(0.0, 0.0)):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.center = center
    
    def __repr__(self):
        return "Triangle(side_1={s1}, side_2={s2}, side_3={s3} center={c})".format(s1=self.side_1,
                                                                                   s2=self.side_2,
                                                                                   s3=self.side_3,
                                                                                   c=self.center)
    
    def compute_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def is_real_triangle(self):
        # sort the sides from least to greatest
        smallest, medium, largest = sorted([self.side_1, self.side_2, self.side_3])

        # return true
        return smallest + medium > largest

class EquilateralTriangle(Triangle):
    def __init__(self, side, center=(0.0, 0.0)):
        super().__init__(side, side, side, center)
    
    def __repr__(self):
        return "EquilateralTriangle(side={s}, center={c})".format(s=self.side1,
                                                                  c=self.center)
    
    def compute_area(self):
        # it doesn't matter which side you use since the triangle is equilateral
        return math.sqrt(3)/2 * (self.side_1 ** 2)/2

t1 = Triangle(2, 3, 4)

print(t1.is_real_triangle())
