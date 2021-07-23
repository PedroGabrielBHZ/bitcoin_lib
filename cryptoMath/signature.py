from hashlib import sha256
from s256 import S256Point, G, N

class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self) -> str:
        return "Signature({:x}, {:x})".format(self.r, self.s)

    def der(self):
        """distinguished encoding rules format"""
        rbin = self.r.to_bytes(32, byteorder='big')
        # remove all null bytes at the beginning
        rbin = rbin.lstrip(b'\x00')
        # if rbin has a high bit, add a \x00
        if rbin[0] & 0x80:
            rbin = b'\x00' + rbin
        result = bytes([2, len(rbin)]) + rbin
        sbin = self.s.to_bytes(32, byteorder="big")
        # remove all null bytes at the beginning
        sbin = sbin.lstrip(b'\x00')
        # if sbin has a high bit, add a \x00
        if sbin[0] & 0x80:
            sbin = b'\x00' + sbin
        result += bytes([2, len(sbin)]) + sbin
        return bytes([0x30, len(result)]) + result

if __name__ == "__main__":

    s = Signature(
        r=0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6,
        s=0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
    )
    print(s.der().hex())