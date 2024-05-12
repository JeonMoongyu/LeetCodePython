class Solution:
    def toHex(self, num: int) -> str:
        
        def f(k: int) -> str:
            if k <= 9:
                return str(k)
            if k == 10:
                return 'a'
            if k == 11:
                return 'b'
            if k == 12:
                return 'c'
            if k == 13:
                return 'd'
            if k == 14:
                return 'e'
            if k == 15:
                return 'f'
        
        if num == 0:
            return "0"
        
        if num < 0:
            num += 2**32
        
        out = []
        while num > 0:
            out.append(f(num%16))
            num //= 16
        return ''.join(out[::-1])