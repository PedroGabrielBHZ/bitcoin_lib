class Point:
    """Represent a point on an elliptic curve."""

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if y**2 != x**3 + a * x + b:
            raise ValueError(f'({x}, {y}) is not on the curve.')

    def __add__(self, o: object) -> object:
        if self.a != o.a or self.b != o.b:
            raise TypeError(f'Points {self}, {o} are not on the same curve.')
        # self is the point at infinity
        if self.x is None:
            return o
        # other is the point at infinity
        if o.x is None:
            return self
        # two points are additive inverses
        if self.x == o.x and self.y != o.y:
            return __class__(None, None, self.a, self.b)

        # general case
        if self.x != o.x:
            s = (o.y - self.y) / (o.x - self.x)
            x_3 = s**2 - self.x - o.x
            y_3 = s * (self.x - x_3) - self.y
            return __class__(x_3, y_3, self.a, self.b)

        # points are equal
        if self == o:
            if self.y == 0 * self.x:
                return self.__class__(None, None, self.a, self.b)
            else:
                s = (3 * o.x**2 + o.a) / (2 * o.y)
                x_3 = s**2 - 2 * o.x
                y_3 = s * (o.x - x_3) - o.y
                return __class__(x_3, y_3, self.a, self.b)

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y \
            and self.a == o.a and self.b == o.b

    def __ne__(self, o: object) -> bool:
        return not (self == o)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


if __name__ == "__main__":
    p1 = Point(-1, 1, 5, 7)
    c = p1 + p1
    print(c)
