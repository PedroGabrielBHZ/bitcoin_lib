class FieldElement:
    """Represent an element in a field F_prime."""

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f'Num {num} not in the field range 0 to {prime - 1}.'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f'FieldElement_{self.prime}({self.num})'

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

        

if __name__ == "__main__":
    a = FieldElement(7, 13)
    print('a = ', a)

    b = FieldElement(6, 13)
    print('b = ', b)

    print('Is a == b? ', a==b)
    print('Is a != b? ', a!=b)
    print('Is a == a? ', a==a)

    print('a - a = ', a - a)
    print('b - b = ', b - b)
    print('a - b = ', a - b)
    print('a + b = ', a + b)
    print('b + b = ', b + b)
    print('a + a = ', a + a)
    
    

