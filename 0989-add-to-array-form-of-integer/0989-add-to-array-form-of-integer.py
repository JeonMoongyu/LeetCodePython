class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        num.reverse()
        k = list(map(int,str(k)))[::-1]
        
        if len(k) > len(num):
            num, k = k, num
        k += [0] * (len(num)-len(k))
        
        r = 0
        for i in range(len(num)):
            num[i], r = (num[i] + k[i] + r)%10, (num[i] + k[i] + r)//10
        if r == 1:
            num += [1]
        num.reverse()
        return num
        