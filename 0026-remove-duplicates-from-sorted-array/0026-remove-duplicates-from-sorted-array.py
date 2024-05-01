class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[cur] = nums[i]
                cur += 1
        return cur