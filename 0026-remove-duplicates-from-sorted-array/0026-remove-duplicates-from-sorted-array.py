class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        cur = 0
        for i in range(1, len(nums)):
            if nums[cur] != nums[i]:
                cur += 1
                k += 1
                nums[cur], nums[i] = nums[i], nums[cur]
        return k