class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour = [8,4,2,1]
        minute = [32,16,8,4,2,1]
        
        def helper(l, n):
            if l == 0:
                return [[]]
            if n == 0:
                return [ [0] * l ]
            out = []
            if l > n:
                for arr in helper(l-1, n):
                    out.append(arr + [0])
            for arr in helper(l-1, n-1):
                out.append(arr + [1])
            return out
        
        
        h, m = 0, 0
        out = []
        for arr in helper(10, turnedOn):
            for i in range(4):
                h += hour[i] * arr[i]
            for i in range(4,10):
                m += minute[i-4] * arr[i]
            if h <= 11 and m <= 59:
                h = str(h)
                m = '0' + str(m) if m <= 9 else str(m)
                out.append(h+":"+m)
            h, m = 0, 0
        return out