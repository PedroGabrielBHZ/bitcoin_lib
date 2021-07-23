from hashlib import sha256
from s256 import S256Point, G, N

class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self) -> str:
        return "Signature({:x}, {:x})".format(self.r, self.s)

if __name__ == "__main__":

    def hash256(s):
        return sha256(sha256(s).digest()).digest()

    e = int.from_bytes(hash256(b'a dirty secret'), 'big')
    z = int.from_bytes(hash256(b'a nice message'), 'big')
    k = 1234567890

    r = (k*G).x.num
    k_inv = pow(k, N-2, N)
    s = (z+r*e) * k_inv % N
    point = e*G

    print('Point: ', point)
    print('Z: ', hex(z))
    print('R: ', hex(r))
    print('S: ', hex(s))

