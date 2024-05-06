class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        out = []
        for num in nums:
            out += list(map(int,str(num)))
        return out