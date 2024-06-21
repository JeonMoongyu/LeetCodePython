class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        out = curr = sum(nums[:k])
        for i in range(len(nums)-k):
            curr = curr - nums[i] + nums[i+k]
            out = max(out, curr)
        return out / k