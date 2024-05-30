class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        out = curr = 1
        for a, b in zip(nums[:-1], nums[1:]):
            if a < b:
                curr += 1
            else:
                out = max(out, curr)
                curr = 1
        out = max(out,curr)
        return out