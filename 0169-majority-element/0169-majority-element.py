class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        M = dict()
        for num in nums:
            if num in M:
                M[num] += 1
            else:
                M[num] = 1
        for num in M:
            if M[num] > len(nums) // 2:
                return num
            