class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                out = [nums[left]**2] + out
                left += 1
            else:
                out = [nums[right]**2] + out
                right -= 1
        return out