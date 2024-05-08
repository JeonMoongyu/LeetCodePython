class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = 0, 1
        n = len(nums)
        while b < n:
            if nums[a] != 0:
                a += 1
                b += 1
            elif nums[b] == 0:
                b += 1
            else:
                nums[a], nums[b]= nums[b], nums[a]
                a += 1
                b += 1