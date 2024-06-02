class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        left = {nums[0]:1}
        right = {}
        for i in range(1, len(nums)):
            if nums[i] in right:
                right[nums[i]] += 1
            else:
                right[nums[i]] = 1
        diff = [ 0 for _ in range(len(nums)) ]
        diff[0] = len(left.keys()) - len(right.keys())
        for i in range(1, len(nums)):
            if nums[i] in left:
                left[nums[i]] += 1
            else:
                left[nums[i]] = 1
            if nums[i] in right:
                if right[nums[i]] == 1:
                    del right[nums[i]]
                else:
                    right[nums[i]] -= 1
            print(left, right)
            diff[i] = len(left.keys()) - len(right.keys())
        return diff