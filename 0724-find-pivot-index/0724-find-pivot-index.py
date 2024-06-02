class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        leftSum = 0 
        rightSum = sum(nums[1:])
        out = 0
        
        while out < n-1:
            print(leftSum, rightSum, out)
            if leftSum == rightSum:
                return out
            leftSum += nums[out]
            rightSum -= nums[out+1]
            out += 1
        
        
        return n-1 if leftSum == rightSum else -1        
        