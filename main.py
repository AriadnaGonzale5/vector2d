import math
class Vector2d:

    def __init__(self,x,y):
        self.x =x
        self.y =y

    def __repr__(self):
        return f"Vector2d(x ='{self.x}', y={self.y})"
    def __str__(self):
        return f"('{self.x}j + {self.y}j')"
    def __abs__(self):
        tempx =self.x**2
        tempy = self.y**2
        soon = tempx + tempy
        done = math.sqrt(soon)
        return done