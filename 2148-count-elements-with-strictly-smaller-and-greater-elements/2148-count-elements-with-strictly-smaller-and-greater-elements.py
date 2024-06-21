class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
       
        minVal = nums[0]
        maxVal = nums[-1]
        if minVal == maxVal:
            return 0
        
        n = len(nums)
        k = 1
        while k < n and minVal == nums[k]:
            k += 1
        
        l = n - 2
        while l >= 0 and maxVal == nums[l]:
            l -= 1
        
        return l - k + 1