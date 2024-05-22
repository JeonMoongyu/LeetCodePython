class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        diff = [ num2 - num1 for num1, num2 in zip(nums[:-1], nums[1:]) ]
        return min([ sum(diff[i:i+k-1]) for i in range(len(diff)-k+2) ])
            