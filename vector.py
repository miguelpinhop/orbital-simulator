class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def __pow__(self, scalar):
        return Vector(self.x ** scalar, self.y ** scalar)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def __truediv__(self, scalar):
        return Vector(self.x/scalar, self.y/scalar)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def dot_product(self, vector):
        result_x = self.x * vector.x
        result_y = self.y + vector.y
        return result_x + result_y
    
    def mag(self): 
        return (self.x**2 + self.y**2)**(1/2)
    
    def normalize(self):
        mag = self.mag()
        if mag == 0:
            return Vector(0, 0)
        x_normalized = self.x/mag
        y_normalized = self.y/mag
        return Vector(x_normalized, y_normalized)
    
    def copy(self):
        return Vector(self.x, self.y)
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False