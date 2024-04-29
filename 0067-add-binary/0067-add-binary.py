class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a10 = 0
        b10 = 0
        for i in a:
            a10 = 2 * a10 + int(i)
        for j in b:
            b10 = 2 * b10 + int(j)
        out10 = a10 + b10
        out2 = []
        if out10 == 0:
            out2 = [0]
        while out10 > 0:
            out2.append(out10%2)
            out10 //= 2
        return ''.join(map(str, out2[::-1]))