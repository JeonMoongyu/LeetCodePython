class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        return sum([nums[i] for i in range(0, len(nums),2)])
    