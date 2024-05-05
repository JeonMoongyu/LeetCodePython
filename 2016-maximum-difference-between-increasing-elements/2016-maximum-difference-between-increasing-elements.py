class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        low = high = nums[0]
        out = -1
        for num in nums[1:]:
            if num < low:
                low = num
                high = num
            elif num > high:
                high = num
            if high > low and high - low > out:
                out = high - low
        return out