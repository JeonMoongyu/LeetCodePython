class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        out, curr = 0, 0
        for num in nums:
            if num == 0:
                out = max(out, curr)
                curr = 0
            else:
                curr += 1
        out = max(out, curr)
        return out