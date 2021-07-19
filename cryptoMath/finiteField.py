class FieldElement:
    """Represent an element in a field F_prime."""

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f'Num {num} not in the field range 0 to {prime - 1}.'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f'F{self.prime}({self.num})'

    def __eq__(self, o: object) -> bool:
        if o is None:
            return False
        return self.num == o.num and self.prime == o.prime

    def __ne__(self, o: object) -> bool:
        if o is None:
            return True
        return self.num != o.num or self.prime != o.prime

    def __add__(self, o: object) -> object:
        if self.prime != o.prime:
            raise TypeError('Cannot add two numbers in different Fields.')
        num = (self.num + o.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, o: object) -> object:
        if self.prime != o.prime:
            raise TypeError('Cannot subtract two numbers in different fields.')
        num = (self.num - o.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, o: object) -> object:
        if self.prime != o.prime:
            raise TypeError('Cannot multiply two numbers in different fields.')
        num = (self.num * o.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int) -> object:
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, o: object) -> object:
        if self.prime != o.prime:
            raise TypeError('Cannot divide two numbers in different fields.')
        # use Fermat's little theorem:
        # self.num ** (p - 1) % p == 1
        # which translates to:
        # 1/n == pow(n, p-2, p)
        num = self.num * pow(o.num, self.prime - 2, self.prime) % self.prime
        return self.__class__(num, self.prime)


if __name__ == "__main__":
    a = FieldElement(2, 19)
    print('a = ', a)

    b = FieldElement(7, 19)
    print('b = ', b)

    print('a / b', a/b)
