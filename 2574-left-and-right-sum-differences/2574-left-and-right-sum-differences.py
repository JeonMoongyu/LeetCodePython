class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0 for _ in range(len(nums))]
        leftSum, rightSum = 0, sum(nums[1:])
        answer[0] = abs(leftSum - rightSum)
        for i in range(1, len(nums)):
            leftSum += nums[i-1]
            rightSum -= nums[i]
            answer[i] = abs(leftSum - rightSum)
        return answer