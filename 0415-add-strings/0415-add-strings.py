class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = list(map(int,num1))[::-1]
        num2 = list(map(int,num2))[::-1]
        num1 += [0] * (len(num2)-len(num1))
        
        out = []
        r = 0
        for k1, k2 in zip(num1, num2):
            out.append((k1+k2+r)%10)
            r = (k1+k2+r) // 10
        if r == 1:
            out.append(1)
        
        out = [ str(elem) for elem in out ]
        return ''.join(out[::-1])
        