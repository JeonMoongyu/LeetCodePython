class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        out = 0
        for num in nums:
            if num < k:
                out += 1
        return out