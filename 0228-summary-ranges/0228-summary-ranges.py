class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        out = []
        i = 0
        for j in range(len(nums)):
            if j == len(nums) - 1 or nums[j+1] > nums[j] + 1:
                if i == j:
                    out += [str(nums[i])]
                else:
                    out += [str(nums[i])+"->"+str(nums[j])]
                i = j + 1
        return out