class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums = [lower-1] + nums + [upper+1]
        out = []
        for a, b in zip(nums[:-1], nums[1:]):
            if b - a > 1:
                out += [(a+1, b-1)]
        return out