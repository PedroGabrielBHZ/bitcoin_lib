class Point:
    """Represent a point on an elliptic curve."""

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # x and y equal to None represents point @ infinity.
        if self.x is None and self.y is None:
            return
        if y**2 != x**3 + a * x + b:
            raise ValueError(f'({x}, {y}) is not on the curve.')

    def __add__(self, o: object) -> object:
        if self.a != o.a or self.b != o.b:
            raise TypeError(f'Points {self}, {o} are not on the same curve.')
        # Case 0.0: self is the point at infinity, return other.
        if self.x is None:
            return o
        # Case 0.1: other is the point at infinity, return self.
        if o.x is None:
            return self
        # Case 1: points are additive inverses: resulting point @ infinity
        if self.x == o.x and self.y != o.y:
            return self.__class__(None, None, self.a, self.b)

        # Case 2: Points have different x's. Apply formulas.
        if self.x != o.x:
            s = (o.y - self.y) / (o.x - self.x)
            x_3 = s**2 - self.x - o.x
            y_3 = s * (self.x - x_3) - self.y
            return self.__class__(x_3, y_3, self.a, self.b)

        # Case 3: Points are equal, but...
        if self == o:
            # ... we are tangent to the vertical line.
            if self.y == 0 * self.x:
                return self.__class__(None, None, self.a, self.b)
            # ... general case, apply formulae:
            else:
                s = (3 * o.x**2 + o.a) / (2 * o.y)
                x_3 = s**2 - 2 * o.x
                y_3 = s * (o.x - x_3) - o.y
                return self.__class__(x_3, y_3, self.a, self.b)

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y \
            and self.a == o.a and self.b == o.b

    def __ne__(self, o: object) -> bool:
        return not (self == o)

    def __repr__(self) -> str:
        if self.x is None:
            return f'P(\u221E)'
        else:
            return f'P({self.x}, {self.y})'

    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result


if __name__ == "__main__":

    from finiteField import FieldElement

    gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
    gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
    p = 2**256 - 2**32 - 977
    if (gy**2 % p) == ((gx**3 + 7) % p):
        print(
            f"Generator point \n({gx}, \n{gy}) is on the curve y^2 = x^3 + 7.")

    n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
    x = FieldElement(gx, p)
    y = FieldElement(gy, p)
    seven = FieldElement(7, p)
    zero = FieldElement(0, p)
    G = Point(x, y, zero, seven)
    print(n*G)
