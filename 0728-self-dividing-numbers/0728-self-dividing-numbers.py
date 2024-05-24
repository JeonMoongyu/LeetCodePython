class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    
        def isSelfDividing(n):
            for m in str(n):
                m = int(m)
                if m == 0 or n % m != 0:
                    return False
            return True
        
        out = []
        for n in range(left, right+1):
            if isSelfDividing(n):
                out.append(n)
        return out