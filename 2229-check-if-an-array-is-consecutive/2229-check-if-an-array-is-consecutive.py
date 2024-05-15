class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        seen = set()
        minNum, maxNum = 10**5, 0
        for num in nums:
            if num in seen:
                return False
            seen.add(num)
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
        return maxNum - minNum == len(nums) - 1
    