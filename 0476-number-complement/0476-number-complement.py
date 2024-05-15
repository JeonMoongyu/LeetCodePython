class Solution:
    def findComplement(self, num: int) -> int:
        arr = []
        while num > 0:
            arr.append(num%2)
            num //= 2
        arr = [ (arr[i]+1)%2 for i in range(len(arr)) ]
        out = 0
        for elem in arr[::-1]:
            out = 2*out + elem
        return out